import requests


class Client():
    def __init__(self, ip='127.0.0.1', port='9999'):
        self.ip = ip
        self.port = port
        self.url = 'http://%s:%s/' % (ip,port)
        # HTTPS support might come eventually, if there's a need
        self.api_new = self.url + 'new/'
        self.api_query = self.url + 'fetch/'
        self.age = self.url + 'age/'
        self.range = self.url + 'range/'
    
    
    def get_from_endpoint(url):
        # reusable function to quickly GET from URL
        response = requests.request(method='GET', url=url)
        data = response.json()
        data = sorted(data, key = lambda i: i['time'])
        return data
    
    
    def send(self, payload):
        # add a new message to the SOC
        response = requests.request(method='POST', url=self.api_new, json=payload)
        print(response.status_code, response.text)
        
    
    def fetch(self, field, keyword):
        # fetch SOC logs based on keyword in the messages
        api_endpoint = self.message + '%s/%s' % (field, keyword)
        data = self.get_from_endpoint(api_endpoint)
        return data
        
    
    def fetch_recent(self, max_age):
        # fetch SOC logs based on recency
        api_endpoint = self.age + str(max_age)
        data = self.get_from_endpoint(api_endpoint)
        return data
        
        
    def fetch_range(self, start, end):
        # fetch SOC logs between two timestamps
        api_endpoint = self.range + '%s/%s' % (start, end)
        data = self.get_from_endpoint(api_endpoint)
        return data