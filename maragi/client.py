import requests


class Client():
    def __init__(self, ip='127.0.0.1', port='9999'):
        self.ip = ip
        self.port = port
        self.url = 'http://%s:%s' % (ip,port)
        # TODO HTTPS support might come eventually, if there's a need
    
    
    def get_from_endpoint(self, url):
        # reusable function to quickly GET from URL
        response = requests.request(method='GET', url=url)
        return response.json()
        
    
    def send(self, service, data, metadata):
        # add a new message to the SOC
        # TODO check that data is JSON-friendly
        # TODO check that metadata is a string
        payload = {'service': service, 'data': data, 'metadata': metadata}
        response = requests.request(method='POST', url=self.api_new, json=payload)
        print(response.status_code, response.text)
        
    
    def get_recent_meta(self, seconds, value):
        # get all message of n seconds old or less with specific value in metadata
        endpoint = self.url + '/recent/meta/%s/%s' % (seconds, value)
        return self.get_from_endpoint(endpoint)
    
    
    def get_recent_data(self, seconds, value):
        # get all message of n seconds old or less with specific value in data
        endpoint = self.url + '/recent/data/%s/%s' % (seconds, value)
        return self.get_from_endpoint(endpoint)
    
    
    def get_recent(self, seconds):
        # get all message of n seconds old or less 
        endpoint = self.url + '/recent/seconds/%s' % seconds
        return self.get_from_endpoint(endpoint)
    
    
    def get_all(self):
        # get all messages
        endpoint = self.url + '/all'
        return self.get_from_endpoint(endpoint)
    
    
    def get_uuid(self, uuid):
        # get all messages
        endpoint = self.url + '/uuid'
        return self.get_from_endpoint(endpoint)

    
    def get_range(self, start, end):
        # fetch SOC logs between two timestamps
        endpoint = self.url + '/range/%s/%s' % (start, end)
        return self.get_from_endpoint(endpoint)