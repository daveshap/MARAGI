import requests


class Client():
    def __init__(self, ip='127.0.0.1', port='9999', api='v1'):
        self.ip = ip
        self.port = port
        self.url = 'http://%s:%s' % (ip,port)
        self.api_new = self.url + '/api/%s/new' % api
        self.api_fetch = self.url + '/api/%s/fetch' % api
        # TODO HTTPS support might come eventually, if there's a need
    
    
    def send(self, payload):
        # add a new message to the SOC
        # payload requires fields: service, metadata, data
        response = requests.request(method='POST', url=self.api_new, json=payload)
        print(response.url, response.ok, response.status_code)
        return response
    
    
    def fetch(self, query):
        # send a search query and get the results
        response = requests.request(method='POST', url=self.api_fetch, json=query)
        print(response.url, response.ok, response.status_code)
        return response.json()