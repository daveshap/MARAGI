import flask
import json
from time import time
from flask import request
from uuid import uuid4
import os
from pprint import pprint


app_port = 9999
app = flask.Flask(__name__)
soc_filename = 'soc.json'
last_save = time()
save_periodicity = 2


def load_stream():
    try:
        with open(soc_filename, 'r') as infile:
            data = json.load(infile)
        return data
    except:
        return []


def filter_stream(max_seconds):
    max_age = time() - int(max_seconds)
    return [i for i in soc_log if i['time']>max_age]


def save_soc_log():
    global last_save
    save_age = time() - last_save
    print('[SAVE AGE]', save_age)
    if save_age > save_periodicity:
        last_save = time()
        with open(soc_filename, 'w') as outfile:
            json.dump(soc_log, outfile, separators=(',\n', ':'))
        print('log saved')


def validate_payload(payload):
    try:
        a = payload['time']
        a = payload['class']
        a = payload['metadata']
        a = payload['message']
        a = payload['service']
        return True
    except:
        return False


def post_new_entry(payload):
    payload['time'] = time()
    valid = validate_payload(payload)
    if valid:
        soc_log.append(payload)
        #print('[NEW LOG]',payload)
        # check age and save
        save_soc_log()
        pprint(payload)
        return 'Log accepted', 200
    else:
        return 'Log rejected', 400


@app.route('/', methods=['POST', 'GET'])
def home():
    # GET the default of 600 seconds
    if request.method == 'GET':
        payload = filter_stream(max_seconds=600)
        return flask.Response(json.dumps(payload), mimetype='application/json')
    
    # POST new entry
    elif request.method == 'POST':
        result = post_new_entry(request.json)
        return result


@app.route('/age/<seconds>', methods=['GET'])
def query_age(seconds):
    # return SOC entries that are N seconds old or newer
    payload = filter_stream(max_seconds=seconds)
    return flask.Response(json.dumps(payload), mimetype='application/json')


@app.route('/class/<keyword>', methods=['GET'])
def query_class(keyword):
    # return SOC entries of a specified class
    payload = [i for i in soc_log if keyword in i['class']]
    return flask.Response(json.dumps(payload), mimetype='application/json')


@app.route('/metadata/<keyword>', methods=['GET'])
def query_metadata(keyword):
    # return SOC entries with specific metadata tags
    payload = [i for i in soc_log if keyword in i['metadata']]
    return flask.Response(json.dumps(payload), mimetype='application/json')
    

@app.route('/range/<start>/<end>', methods=['GET'])
def query_range(start, end):
    # return SOC entries between two specified unix epoch timestamps
    payload = [i for i in soc_log if i['time']>=int(start) and i['time']<=int(end)]
    return flask.Response(json.dumps(payload), mimetype='application/json')


@app.route('/message/<keyword>', methods=['GET'])
def query_message(keyword):
    # return SOC entries with specific keyword in the message
    payload = [i for i in soc_log if keyword.lower() in i['message'].lower()]
    return flask.Response(json.dumps(payload), mimetype='application/json')


if __name__ == '__main__':
    soc_log = load_stream()
    post_new_entry({'time': time(), 'class': 'system', 'subclass': 'service start', 'service': 'soc_service', 'message': 'SOC service has started'})
    app.run(host='0.0.0.0', port=app_port)