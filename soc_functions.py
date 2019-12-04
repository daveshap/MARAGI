import requests
import json
from time import time, sleep


soc_port = 9999
soc_url = 'http://127.0.0.1:%s/' % soc_port
age_api = soc_url + 'age/'
class_api = soc_url + 'class/'
subclass_api = soc_url + 'subclass/'
range_api = soc_url + 'range/'
service_api = soc_url + 'service/'


def get_from_endpoint(url):
    response = requests.request(method='GET', url=url)
    data = response.json()
    data = sorted(data, key = lambda i: i['time'])
    return data


def fetch_soc_age(max_seconds=600):
    api_endpoint = age_api + '%s' % max_seconds
    return get_from_endpoint(api_endpoint)


def add_soc_log(clss, subclass, service, message):
    payload = {'time': time(), 'class': clss, 'subclass': subclass, 'message': message, 'service': service}
    response = requests.request(method='POST', url=soc_url, json=payload)
    return response.ok


def fetch_soc_class(class_name):
    api_endpoint = class_api + class_name
    return get_from_endpoint(api_endpoint)


def fetch_soc_subclass(subclass):
    api_endpoint = subclass_api + subclass
    return get_from_endpoint(api_endpoint)
    
    
def fetch_soc_range(start, end):
    api_endpoint = soc_url + '%s/%s' % (start, end)
    return get_from_endpoint(api_endpoint)


def fetch_soc_service(service):
    api_endpoint = service_api + service
    return get_from_endpoint(api_endpoint)


if __name__ == '__main__':
    print('[FETCH LOG]',fetch_soc_age())
    print('[ADD LOG]', add_soc_log('system', 'test', 'soc_test', 'this is a test message'))