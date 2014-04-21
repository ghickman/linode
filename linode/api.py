import sys
from warnings import warn

import requests

from .params import get_required_params


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
        self._params = get_required_params(self.endpoint)

    def __getattr__(self, name):
        return Worker(self, [name])

    def _build_api_kwargs(self, action, *args, **kwargs):
        if args:
            action_required_params = list(self._params[action])
            try:
                kwargs.update(dict(
                    [(action_required_params.pop(0), arg) for arg in args]))
            except IndexError:
                raise TypeError('Too many non-keyword'
                                'arguments for {0}'.format(action))

        kwargs.update({'api_key': self._api_key, 'api_action': action})
        return kwargs

    def _request(self, payload):
        r = requests.post(self.endpoint, data=payload)
        if r.status_code == requests.codes.ok:
            content = r.json()
            if content.get('ERRORARRAY'):
                raise LinodeException(content.get('ACTION'), content.get('ERRORARRAY'))
            return content.get('DATA')

    def _worker_func(self, path, *args, **kwargs):
        "Function called at the end of the object chain"
        action = '.'.join(path)
        api_kwargs = self._build_api_kwargs(action, *args, **kwargs)
        return self._request(api_kwargs)

