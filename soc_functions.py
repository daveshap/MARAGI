import requests
import json
from time import time, sleep


soc_port = 9999
soc_url = 'http://127.0.0.1:%s/' % soc_port
age_api = soc_url + 'age/'
metadata_api = soc_url + 'metadata/'
range_api = soc_url + 'range/'
origin_api = soc_url + 'origin/'
message_api = soc_url + 'message/'


def get_from_endpoint(url):
    response = requests.request(method='GET', url=url)
    data = response.json()
    data = sorted(data, key = lambda i: i['time'])
    return data


def fetch_soc_age(max_seconds=600):
    api_endpoint = age_api + '%s' % max_seconds
    return get_from_endpoint(api_endpoint)


def fetch_soc_message(keyword):
    api_endpoint = message_api + keyword
    return get_from_endpoint(api_endpoint)
    

def add_soc_log(metadata, origin, message):
    payload = {'metadata': metadata, 'message': message, 'origin': origin}
    response = requests.request(method='POST', url=soc_url, json=payload)
    return response.ok


def fetch_soc_metadata(metadata):
    api_endpoint = metadata_api + metadata
    return get_from_endpoint(api_endpoint)
    
    
def fetch_soc_range(start, end):
    api_endpoint = soc_url + '%s/%s' % (start, end)
    return get_from_endpoint(api_endpoint)


def fetch_soc_origin(origin):
    api_endpoint = origin_api + origin
    return get_from_endpoint(api_endpoint)


if __name__ == '__main__':
    print('[FETCH LOG]',fetch_soc_age())
    print('[ADD LOG]', add_soc_log('system', 'test', 'soc_test', 'this is a test message'))