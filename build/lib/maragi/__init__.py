import flask
import json
from time import time
from flask import request
from uuid import uuid4
import requests


class Server():
    def __init__(self, port=9999, fields=[], soc_file='soc.json'):
        self.port = port
        self.soc_file = soc_file
        self.fields = fields + ['time', 'uuid', 'service']
        self.soc_log = []


    def validate_message(self, message):
        # check message against SOC fields
        try:
            for field in self.fields:
                a = payload[field]
        except:
            return False
        return True


    def load_soc(self):
        # run this separate to reload SOC file, otherwise it will be overwritten
        with open(self.soc_file, 'r') as infile:
            temp_log = json.load(infile)
        for log in temp_log:
            if not self.validate_message(log):
                print('Log missing necessary fields')
                return 
        self.soc_log = temp_log
        print('SOC log loaded')


    def run(self):
        app = flask.Flask('maragi')
        
        @app.route('/new', methods=['POST'])
        # register a new message with the SOC
        def new_message():
            payload = request.json
            payload['time'] = str(time())
            payload['uuid'] = str(uuid4())
            if self.validate_message(payload):
                self.soc_log.append(payload)
                with open(self.soc_file, 'w') as outfile:
                    json.dump(self.soc_log, outfile, separators=(',\n ', ': '))
                return 'Log accepted and saved', 200
            else:
                return 'Log rejected, missing field', 402

        @app.route('/fetch/<field>/<keyword>', methods=['GET'])
        # return all messages from SOC where a particular term is in a specified field
        def fetch_field(field, keyword):
            result = [i for i in self.soc_log if keyword.lower() in i[field].lower()]
            return flask.Response(json.dumps(result), mimetype='application/json')

        @app.route('/age/<seconds>', methods=['GET'])
        # return SOC entries that are N seconds old or newer
        def fetch_logs_age(seconds):
            max_age = time() - int(seconds)
            payload = [i for i in self.soc_log if i['time']>max_age]
            return flask.Response(json.dumps(payload), mimetype='application/json')
           
        @app.route('/range/<start>/<end>', methods=['GET'])
        # return SOC entries between two specified unix epoch timestamps
        def fetch_logs_range(start, end):
            payload = [i for i in self.soc_log if i['time']>=int(start) and i['time']<=int(end)]
            return flask.Response(json.dumps(payload), mimetype='application/json')

        @app.route('/all', methods=['GET'])
        # return all SOC messages
        def fetch_all():
            return flask.Response(json.dumps(self.soc_log), mimetype='application/json')
            
        @app.route('/fields', methods=['GET'])
        # return list of fields current SOC is using
        def get_fields():
            return flask.Response(json.dumps(self.fields), mimetype='application/json')
            
        app.run(host='0.0.0.0', port=self.port)
        
        
class Client():
    def __init__(self, ip='127.0.0.1', port='9999'):
        self.ip = ip
        self.port = port
        self.url = 'http://%s:%s/' % (ip,port)
        # HTTPS support might come eventually, if there's a need
        self.api_new = self.url + 'new/'
        self.api_query = self.url + 'fetch/'
        self.age = self.url + 'age/'
        self.range = self.url + 'range/'
    
    
    def get_from_endpoint(url):
        # reusable function to quickly GET from URL
        response = requests.request(method='GET', url=url)
        data = response.json()
        data = sorted(data, key = lambda i: i['time'])
        return data
    
    
    def send(self, payload):
        # add a new message to the SOC
        response = requests.request(method='POST', url=self.api_new, json=payload)
        print(response.status_code, response.text)
        
    
    def fetch(self, field, keyword):
        # fetch SOC logs based on keyword in the messages
        api_endpoint = self.message + '%s/%s' % (field, keyword)
        data = self.get_from_endpoint(api_endpoint)
        return data
        
    
    def fetch_recent(self, max_age):
        # fetch SOC logs based on recency
        api_endpoint = self.age + str(max_age)
        data = self.get_from_endpoint(api_endpoint)
        return data
        
        
    def fetch_range(self, start, end):
        # fetch SOC logs between two timestamps
        api_endpoint = self.range + '%s/%s' % (start, end)
        data = self.get_from_endpoint(api_endpoint)
        return data