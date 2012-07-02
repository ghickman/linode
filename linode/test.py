import contextlib
import json
import sys
from unittest import TestCase
from warnings import catch_warnings

from mock import patch
from nose.tools import assert_equal, assert_raises, assert_true
import requests

from .api import Api, LinodeException, Worker


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
requests.post = good_post


@contextlib.contextmanager
def nostderr():
    """
    Courtesy of Alex Martelli:
    http://stackoverflow.com/questions/1809958/hide-stderr-output-in-unit-tests/1810086#1810086
    """
    savestderr = sys.stderr
    class Devnull(object):
        def write(self, _): pass
    sys.stderr = Devnull()
    yield
    sys.stderr = savestderr


class BaseTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(BaseTest, self).__init__(*args, **kwargs)
        self.api = Api('api_key')


class ApiKwargsTest(BaseTest):
    def test_args_are_converted_to_kwargs(self):
        action = 'linode.boot'
        ideal_kwargs = {'api_key': self.api._api_key, 'api_action': action,
                        'linodeid': 'herp'}
        actual_kwargs = self.api._build_api_kwargs(action, 'herp')
        assert_equal(actual_kwargs, ideal_kwargs)

    def test_kwargs_are_passed_into_api_kwargs(self):
        action = 'avail.distributions'
        ideal_kwargs = {'api_key': self.api._api_key, 'api_action': action,
                        'distributionid': 1}
        actual_kwargs = self.api._build_api_kwargs(action, distributionid=1)
        assert_equal(actual_kwargs, ideal_kwargs)

    def test_passing_args_when_only_optional_args_are_allowed(self):
        with catch_warnings(record=True) as w:
            assert_raises(TypeError, self.api._build_api_kwargs, 'linode.list', 'herp')
            assert len(w) == 1
            assert issubclass(w[-1].category, SyntaxWarning)

    def test_passing_too_many_arguments(self):
        assert_raises(TypeError, self.api._build_api_kwargs, 'linode.create',
                      'herp', 'derp', 'foo', 'bar')


class ApiTest(BaseTest):
    def test_instantiate_api_without_key_throws_exception(self):
        assert_raises(Exception, Api)

    def test_getattr_returns_worker_class(self):
        assert_equal(type(self.api._api_key), type(str()))
        assert_equal(type(self.api.linode), Worker)

    @patch('requests.post', new=bad_post)
    def test_linode_exception_raised_when_error_returned(self):
        payload = {'api_key': self.api._api_key, 'api_action': 'linode.create'}
        with nostderr():
            assert_raises(LinodeException, self.api._request, payload)


class WorkerTest(BaseTest):
    def test_worker_instantiated_with_path_and_klass(self):
        worker = self.api.linode
        assert_true(worker.klass)
        assert_true(worker.path)
        assert_equal(worker.klass.__class__.__name__, 'Api')
        assert_equal(worker.path, ['linode'])

    def test_sub_worker_path_built_from_action(self):
        worker = self.api.linode.disk
        assert_equal(worker.klass.__class__.__name__, 'Api')
        assert_equal(worker.path, ['linode', 'disk'])


