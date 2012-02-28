import requests


class Base(object):
    endpoint = 'https://api.linode.com/'

    def __init__(self, api_key, parent_namespace=None):
        self.api_key = api_key
        if parent_namespace:
            self.namespace = parent_namespace + self.namespace

    def request(self, action, **kwargs):
        payload = {'api_key': self.api_key, 'api_action': action}
        payload.update(kwargs)
        return requests.post(self.endpoint, data=payload)

