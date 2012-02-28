import requests


class Base(object):
    endpoint = 'https://api.linode.com/'

    def __init__(self, api_key):
        self.api_key = api_key

    def request(self, action, **kwargs):
        payload = {'api_key': self.api_key, 'api_action': action}
        payload.update(kwargs)
        return requests.post(self.endpoint, data=payload)

