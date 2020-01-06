import flask
import json
from time import time
from flask import request
from uuid import uuid4


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
            return flask.Response(json.dumps(self.fields), mimetype='application/json')
            
        app.run(host='0.0.0.0', port=self.port)
        
        
