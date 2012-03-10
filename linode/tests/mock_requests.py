import json

from minimock import mock
import requests


class Post(object):
    """Mock requests' Response object when called from requests.post"""
    def __init__(self, action, bad=False):
        content = {'ACTION': action, 'DATA': ''}
        self.status_code = requests.codes.ok
        if bad:
            content['ERRORARRAY'] = [{'ERRORCODE': 4, 'ERRORMESSAGE': 'oh noes'}]
        self.content = json.dumps(content)


def bad_post(url, data=None, **kwargs):
    return Post(data['api_action'], bad=True)


def good_post(url, data=None, **kwargs):
    return Post(data['api_action'])


mock('requests.post', returns_func=good_post, tracker=None)

