import flask
import json
from time import time
from flask import request
from uuid import uuid4


class Server():
    def __init__(self, port=9999):
        self.port = port
        self.fields = ['time', 'uuid', 'service', 'data', 'metadata']
        self.soc_log = []
        # TODO save to file
        # TODO ship to syslog
        # TODO ship to AMQP


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


    def filter_age(self, seconds):
        max_age = time() - int(seconds)
        result = [i for i in self.soc_log if i['time']>=max_age]
        return result       


    def filter_field(self, field, value):
        result = [i for i in self.soc_log if value.lower() in i[field].lower()]
        return result


    def run(self):
        app = flask.Flask('maragi')
        
        @app.route('/new', methods=['POST'])
        # register a new message with the SOC
        def new_message():
            payload = request.json
            payload['time'] = time()
            payload['uuid'] = str(uuid4())
            if self.validate_message(payload):
                self.soc_log.append(payload)
                print(payload)
                return 'Log accepted and saved', 200
            else:
                return 'Log rejected, missing field', 402

        @app.route('/recent/meta/<seconds>/<value>', methods=['GET'])
        # fetch most recent messages of age n seconds or less that match a certain field in the metadata
        def recent_meta(seconds,value):
            recent = filter_age(seconds)
            result = filter_field('metadata', value)
            return flask.Response(json.dumps(result), mimetype='application/json')
        
        @app.route('/recent/data/<seconds>/<value>', methods=['GET'])
        # fetch most recent messages of age n seconds or less that match a certain field in the data
        def recent_data(seconds,value):
            recent = filter_age(seconds)
            result = filter_field('data', value)
            return flask.Response(json.dumps(result), mimetype='application/json')
        
        @app.route('/recent/seconds/<seconds>', methods=['GET'])
        # fetch all messages within certain age
        def recent_seconds(seconds):
            recent = filter_age(seconds)
            return flask.Response(json.dumps(recent), mimetype='application/json')
        
        @app.route('/range/<start>/<end>', methods=['GET'])
        # return SOC entries between two specified unix epoch timestamps
        def fetch_range(start, end):
            payload = [i for i in self.soc_log if i['time']>=int(start) and i['time']<=int(end)]
            return flask.Response(json.dumps(payload), mimetype='application/json')

        @app.route('/all', methods=['GET'])
        # return all SOC messages
        def fetch_all():
            return flask.Response(json.dumps(self.soc_log), mimetype='application/json')
            
        @app.route('/uuid/<uuid>', methods=['GET'])
        # return specific UUID
        def fetch_uuid(uuid):
            result = [i for i in self.soc_log if i['uuid']==uuid]
            return flask.Response(json.dumps(result), mimetype='application/json')
            
        app.run(host='0.0.0.0', port=self.port)
        
        
