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
        try:
            for field in self.fields:
                a = message[field]
            return True
        except Exception as oops:
            print(oops)
            return False
        
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
        with open('./static/head.html', 'r') as infile:
            html = infile.read()
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
            if self.validate_message(payload):
                self.soc_log.append(payload)
                return 'Log accepted and saved', 200
            else:
                return 'Log rejected, missing field', 402

        @app.route('/api/v1/fetch', methods=['POST'])
        def api_v1_fetch():
            payload = request.json
            result = self.filter_soc(payload)
            return flask.Response(json.dumps(result), mimetype='application/json')

        app.run(host='0.0.0.0', port=self.port)