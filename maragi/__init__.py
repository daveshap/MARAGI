import requests
import os
import flask
import json
from time import time
from flask import request
from uuid import uuid4


class Server():
    def __init__(self, port=9999, fields=['time', 'uuid', 'service', 'data', 'metadata']):
        self.port = port
        self.fields = fields
        self.soc_log = []
        # TODO save to file
        # TODO ship to syslog
        # TODO ship to AMQP


    def validate_message(self, message):
        # check message against SOC fields
        result = {}
        try:
            for field in self.fields:
                result[field] = message[field]
            return True, result
        except Exception as oops:
            print(oops)
            return False, str(oops)

        
    def filter_soc(self, query):
        # TODO
        # Example {start: time, end: time}
        # Example {uuid: uuid}
        # Example {service: service}
        # Example {metadata: {cortex: vision, type: image}}
        everything = self.soc_log
        for qkey in query.keys():
            if qkey == 'start':
                everything = [i for i in everything if float(i['time']) >= float(query['start'])]
            if qkey == 'end':
                everything = [i for i in everything if float(i['time']) <= float(query['end'])]
            if qkey == 'uuid':
                everything = [i for i in everything if i['uuid'] == query['uuid']]
            if qkey == 'service':
                everything = [i for i in everything if i['service'] == query['service']]
            if qkey == 'metadata':
                metadata = query['metadata']
                for mkey in metadata.keys():
                    everything = [i for i in everything if i['metadata'][mkey] == metadata[mkey]]
        return everything


    def html_head(self):
        html = """<html>
<head>
	<title>MARAGI Server</title>
	<link rel="shortcut icon" href="/favicon.ico">
</head>

<body>
<h1>Welcome to MARAGI</h1>
"""
        return html


    def run(self):
        app = flask.Flask('maragi')
        
        @app.route('/favicon.ico')
        def favicon():
            return flask.send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
        
        @app.route('/', methods=['POST', 'GET'])
        def home():
            return flask.redirect('/web')
            
        @app.route('/web', methods=['GET'])
        def web_root():
            # TODO
            html = self.html_head()
            data = sorted(self.soc_log, key=lambda i: i['time'], reverse=True)
            data = data[0:100]
            html += '<pre>\n'
            for i in data:
                html += '%s\t%s\t%s\t%s\t%s<br>' % (i['uuid'], i['time'], i['service'], i['metadata'], i['data'])
            html += '</pre>\n</body></html>'
            return flask.Response(html, mimetype='text/html')
        
        @app.route('/api/v1/new', methods=['POST'])
        # register a new message with the SOC
        def api_v1_new():
            payload = request.json
            payload['time'] = time()
            payload['uuid'] = str(uuid4())
            print(payload)
            valid, result = self.validate_message(payload)
            if (valid):
                self.soc_log.append(result)
                return 'Log accepted and saved', 200
            else:
                print(result)
                return 'Log rejected, missing field', 402

        @app.route('/api/v1/fetch', methods=['POST'])
        def api_v1_fetch():
            payload = request.json
            result = self.filter_soc(payload)
            return flask.Response(json.dumps(result), mimetype='application/json')

        app.run(host='0.0.0.0', port=self.port)


class Client():
    def __init__(self, ip='127.0.0.1', port='9999', api='v1'):
        self.ip = ip
        self.port = port
        self.url = 'http://%s:%s' % (ip,port)
        self.api_new = self.url + '/api/%s/new' % api
        self.api_fetch = self.url + '/api/%s/fetch' % api
        self.default_query = {}
        self.default_metadata = {}
        self.service_name = '<service name>'
        # TODO HTTPS support might come eventually, if there's a need
        # TODO multi-server support
        #self.servers = [{'ip': ip, 'port': port, 'api'=api]
    
    
    def send(self, payload):
        # add a new message to the SOC
        if 'metadata' not in payload:
            payload['metadata'] = self.default_metadata
        if 'service' not in payload:
            payload['service'] = self.service_name
        response = requests.request(method='POST', url=self.api_new, json=payload)
        self.last_send = time()
        print(response.url, response.ok, response.status_code)
        return response
    
    
    def fetch(self, query=self.default_query):
        # send a search query and get the results
        response = requests.request(method='POST', url=self.api_fetch, json=query)
        self.last_fetch = time()
        print(response.url, response.ok, response.status_code)
        return response.json()