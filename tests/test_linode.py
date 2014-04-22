import contextlib
import json
import sys

from mock import patch
from pytest import raises
import requests

from linode.api import Api, LinodeException, Worker


class Post(object):
    """Mock requests' Response object when called from requests.post"""
    def __init__(self, action, bad=False):
        content = {'ACTION': action, 'DATA': ''}
        self.status_code = requests.codes.ok
        if bad:
            content['ERRORARRAY'] = [{'ERRORCODE': 4, 'ERRORMESSAGE': 'oh noes'}]
        self.content = content

    def json(self):
        return json.loads(json.dumps(self.content))


def bad_post(url, data=None, **kwargs):
    return Post(data['api_action'], bad=True)


def good_post(url, data=None, **kwargs):
    return Post(data['api_action'])
requests.post = good_post


@contextlib.contextmanager
def nostderr():
    """
    Courtesy of Alex Martelli:
    http://stackoverflow.com/questions/1809958/hide-stderr-output-in-unit-tests/1810086#1810086
    """
    savestderr = sys.stderr

    class Devnull(object):
        def write(self, _):
            pass

    sys.stderr = Devnull()
    yield
    sys.stderr = savestderr


class Base(object):
    api = Api('api_key')


class TestApiKwargs(Base):
    def test_args_are_converted_to_kwargs(self):
        action = 'linode.boot'
        ideal_kwargs = {'api_key': self.api._api_key, 'api_action': action,
                        'linodeid': '1234'}
        actual_kwargs = self.api._build_api_kwargs(action, '1234')
        assert actual_kwargs == ideal_kwargs

    def test_kwargs_are_passed_into_api_kwargs(self):
        action = 'avail.distributions'
        ideal_kwargs = {'api_key': self.api._api_key, 'api_action': action,
                        'distributionid': 1}
        actual_kwargs = self.api._build_api_kwargs(action, distributionid=1)
        assert actual_kwargs == ideal_kwargs

    def test_passing_too_many_arguments(self):
        with raises(TypeError):
            args = ('1234', 'derp', 'foo', 'bar')
            self.api._build_api_kwargs('linode.create', *args)


class TestApi(Base):
    def test_instantiate_api_without_key_throws_exception(self):
        with raises(Exception):
            Api()

    def test_getattr_returns_worker_class(self):
        assert isinstance(self.api._api_key, str)
        assert isinstance(self.api.linode, Worker)

    @patch('requests.post', new=bad_post)
    def test_linode_exception_raised_when_error_returned(self):
        payload = {'api_key': self.api._api_key, 'api_action': 'linode.create'}
        with nostderr():
            with raises(LinodeException):
                self.api._request(payload)


class TestWorker(Base):
    def test_worker_instantiated_with_path_and_klass(self):
        worker = self.api.linode
        assert worker.klass
        assert worker.path
        assert worker.klass.__class__.__name__ == 'Api'
        assert worker.path == ['linode']

    def test_sub_worker_path_built_from_action(self):
        worker = self.api.linode.disk
        assert worker.klass.__class__.__name__ == 'Api'
        assert worker.path == ['linode', 'disk']
