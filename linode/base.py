import json

import requests


class LinodeException(Exception):
    def __init__(self, error_array):
        print 'Error: {0}'.format(error_array[0]['ERRORMESSAGE'])


class Base(object):
    endpoint = 'https://api.linode.com/'

    def __init__(self, api_key, parent_namespace=None):
        self.api_key = api_key
        if parent_namespace:
            self.namespace = parent_namespace + self.namespace

    def build_kwargs(self, clean_locals):
        clean_locals.pop('self')
        return {local.replace('_', ''): clean_locals[local]
                for local in clean_locals if clean_locals[local]}

    def request(self, action, func_locals):
        kwargs = self.build_kwargs(func_locals)
        payload = {'api_key': self.api_key, 'api_action': action}
        payload.update(**kwargs)
        r = requests.post(self.endpoint, data=payload)
        if r.status_code == requests.codes.ok:
            content = json.loads(r.content)
            if content['ERRORARRAY']:
                print content
                raise LinodeException(content['ERRORARRAY'])
            return content['DATA']

