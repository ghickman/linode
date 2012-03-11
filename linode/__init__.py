__title__ = 'linode'
__author__ = 'George Hickman'
__copyright__ = 'Copyright 2012 George Hickman'
__license__ = 'MIT'

__version__ = (0, 1, 0)


# Module namespace.

def get_version():
    return '.'.join(map(str, __version__))

from .api import Api
__all__ = ('Api',)

