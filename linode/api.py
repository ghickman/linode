from .domain import Domain
from .linode import Linode


class Api(object):
    """
    General api class that all other namespacing exists under.
    Instantiate with an api_key and call the other methods on it.
    """

    def __init__(self, api_key):
        self.domain = Domain(api_key)
        self.linode = Linode(api_key)

