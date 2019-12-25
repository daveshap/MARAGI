import requests



class RavenClient():
    def __init__(self, ip=127.0.0.1, port=9999):
        self.ip = ip
        self.port = port
        self.url = 'http://%s:%s/' % (ip,port)
        self.age = self.url + 'age/'
        self.metadata = self.url + 'metadata/'
        self.range = self.url + 'range/'
        self.origin = self.url + 'origin/'
        self.message = self.url + 'message/'
    
    
    def get_from_endpoint(url):
        # reusable function to quickly GET from URL
        response = requests.request(method='GET', url=url)
        data = response.json()
        data = sorted(data, key = lambda i: i['time'])
        return data
    
    
    def add_message(self, metadata, origin, message):
        # add a new message to the SOC
        payload = {'metadata': metadata, 'message': message, 'origin': origin}
        response = requests.request(method='POST', url=self.url, json=payload)
        print(response.status_code, response.text)
        
    
    def fetch_message(self, keyword):
        # fetch SOC logs based on keyword in the messages
        api_endpoint = self.message + keyword
        data = self.get_from_endpoint(api_endpoint)
        return data
        
    
    def fetch_recent(self, max_age):
        api_endpoint = self.age + str(max_age)
        data = self.get_from_endpoint(api_endpoint)
        return data
        
        
    def fetch_range(self, start, end):
        api_endpoint = self.range + '%s/%s' % (start, end)
        data = self.get_from_endpoint(api_endpoint)
        return data
        
        
    def fetch_metadata(self, keyword):
        api_endpoint = self.metadata + keyword
        data = self.get_from_endpoint(api_endpoint)
        return data
        
        
    def fetch_origin(self, keyword):
        api_endpoint = self.origin + keyword
        data = self.get_from_endpoint(api_endpoint)
        return data