from .domain import Domain
from .linode import Linode
from .stackscript import Stackscript
from .utility import Account, Avail


class Api(object):
    """
    General api class that all other namespacing exists under.
    Instantiate with an api_key and call the other methods on it.
    """

    def __init__(self, api_key):
        self.account = Account(api_key)
        self.avail = Avail(api_key)
        self.domain = Domain(api_key)
        self.linode = Linode(api_key)
        self.stackscript = Stackscript(api_key)

