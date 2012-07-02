import json
import sys
from warnings import warn

import requests

from .params import params


class LinodeException(Exception):
    def __init__(self, action, error_array):
        for err in error_array:
            sys.stderr.write('[{0}] {1}'.format(action, err.get('ERRORMESSAGE')))


class Worker(object):
    def __init__(self, klass, path):
        self.klass = klass
        self.path = path

    def __getattr__(self, name):
        return Worker(self.klass, self.path + [name])

    def __call__(self, *args, **kwargs):
        return self.klass._worker_func(self.path, *args, **kwargs)


class Api(object):
    """
    General api class that all other namespacing exists under.
    Instantiate with an api_key and call the other methods on it.
    """
    endpoint = 'https://api.linode.com/'

    def __init__(self, api_key):
        self._api_key = api_key

    def __getattr__(self, name):
        return Worker(self, [name])

    def _build_api_kwargs(self, action, *args, **kwargs):
        if args:
            try:
                action_params = list(params[action])
            except KeyError:
                action_params = []
                warn('{0} only takes optional arguments. Non-keywords arguments '
                     'will be ignored.'.format(action), SyntaxWarning)

            try:
                kwargs.update(dict([(action_params.pop(0), arg) for arg in args]))
            except IndexError:
                raise TypeError('Too many arguments for {0}'.format(action))

        kwargs.update({'api_key': self._api_key, 'api_action': action})
        return kwargs

    def _request(self, payload):
        r = requests.post(self.endpoint, data=payload)
        if r.status_code == requests.codes.ok:
            content = json.loads(r.content)
            if content.get('ERRORARRAY'):
                raise LinodeException(content.get('ACTION'), content.get('ERRORARRAY'))
            return content.get('DATA')

    def _worker_func(self, path, *args, **kwargs):
        "Function called at the end of the object chain"
        action = '.'.join(path)
        api_kwargs = self._build_api_kwargs(action, *args, **kwargs)
        return self._request(api_kwargs)

