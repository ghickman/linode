from os.path import dirname, join
from setuptools import setup, find_packages

from linode import get_version


def fread(fn):
    with open(join(dirname(__file__), fn), 'r') as f:
        return f.read()

setup(
    name = 'linode',
    version = get_version(),
    description = 'Python wrapper of the Linode API',
    long_description = fread('README.md'),
    author = 'George Hickman',
    author_email = 'george@ghickman.co.uk',
    url = 'http://github.com/ghickman/linode',
    license = 'MIT',
    packages = find_packages(),
    install_requires = ('requests',)
)

