import json

import requests


class LinodeException(Exception):
    def __init__(self, action, error_array):
        print '[{0}] {1}'.format(action, error_array[0]['ERRORMESSAGE'])


class Base(object):
    endpoint = 'https://api.linode.com/'

    def __init__(self, api_key, parent_namespace=None):
        self.api_key = api_key
        if parent_namespace:
            self.namespace = parent_namespace + self.namespace

    def build_api_kwargs(self, clean_locals):
        """
        Build the api kwargs dict by removing any None variables so
        the API doesn't think we're trying to set them.
        """
        clean_locals.pop('self')
        return {local: clean_locals[local] for local in clean_locals
                                 if clean_locals[local] is not None}

    def request(self, action, func_locals):
        kwargs = self.build_api_kwargs(func_locals)
        payload = {'api_key': self.api_key, 'api_action': action}
        payload.update(**kwargs)
        r = requests.post(self.endpoint, data=payload)
        if r.status_code == requests.codes.ok:
            content = json.loads(r.content)
            if content['ERRORARRAY']:
                raise LinodeException(content['ACTION'], content['ERRORARRAY'])
            return content['DATA']

