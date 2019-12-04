import json
import requests
from pprint import pprint
from time import time


app_port = 9999
main_url = 'http://127.0.0.1:%s/' % app_port


if __name__ == '__main__':
    start = time()
    response = requests.request(method='GET', url=main_url)
    end = time()
    print('GET response:')
    pprint(response.json())
    print('response time:', end - start)
    #payload = {'time': time(), 'type': 'event', 'subtype': 'test message', 'message': 'this is simply a test of the SOC service'}
    #payload = {}
    #response = requests.request(method='POST', url=main_url, json=payload)
    #print('POST response:')
    #print(response, response.text)