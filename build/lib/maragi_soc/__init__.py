import flask
import json
from time import time
from flask import request


class Server():
    def __init__(self, port=9999, soc_file='soc.json'):
        self.port = port
        self.soc_file = soc_file
        # load SOC
        try:
            with open(self.soc_file, 'r') as infile:
                self.soc_log = json.load(infile)
            print('SOC log loaded')
        except:
            print('SOC log not found, created new log')
            self.soc_log = []
        

    def run(self):
        app = flask.Flask('maragi')
        
        @app.route('/', methods=['POST'])
        def post_log():
            payload = request.json
            payload['time'] = time()
            # validate payload
            try:
                a = payload['time']
                a = payload['metadata']
                a = payload['message']
                a = payload['origin']
                a = payload['label']
            except:
                return 'Log rejected, invalid payload', 400
            # append message
            self.soc_log.append(payload)
            # save log
            with open(self.soc_file, 'w') as outfile:
                json.dump(self.soc_log, outfile, separators=(',\n ', ': '))
            return 'Log accepted and saved', 200

        @app.route('/age/<seconds>', methods=['GET'])
        def fetch_logs_age(seconds):
            # return SOC entries that are N seconds old or newer
            max_age = time() - int(seconds)
            payload = [i for i in self.soc_log if i['time']>max_age]
            return flask.Response(json.dumps(payload), mimetype='application/json')

        @app.route('/metadata/<keyword>', methods=['GET'])
        def fetch_logs_meta(keyword):
            # return SOC entries with specific metadata tags
            payload = [i for i in self.soc_log if keyword in i['metadata']]
            return flask.Response(json.dumps(payload), mimetype='application/json')
            
        @app.route('/range/<start>/<end>', methods=['GET'])
        def fetch_logs_range(start, end):
            # return SOC entries between two specified unix epoch timestamps
            payload = [i for i in self.soc_log if i['time']>=int(start) and i['time']<=int(end)]
            return flask.Response(json.dumps(payload), mimetype='application/json')

        @app.route('/message/<keyword>', methods=['GET'])
        def fetch_logs_message(keyword):
            # return SOC entries with specific keyword in the message
            payload = [i for i in self.soc_log if keyword.lower() in i['message'].lower()]
            return flask.Response(json.dumps(payload), mimetype='application/json')
            
        @app.route('/label/<keyword>', methods=['GET'])
        def fetch_logs_label(keyword):
            # return SOC entries with specific keyword in the message
            payload = [i for i in self.soc_log if keyword.lower() in i['label'].lower()]
            return flask.Response(json.dumps(payload), mimetype='application/json')
            
        app.run(host='0.0.0.0', port=self.port)