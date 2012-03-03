from .base import Base


class Config(Base):
    namespace = 'config.'

    def create(self, nodebalancerid, port=None, protocol=None, algorithm=None,
               stickiness=None, check=None, check_interval=None, check_timeout=None,
               check_attempts=None, check_path=None, check_body=None):
        api_action = self.namespace + 'create'
        return self.request(api_action, locals())

    def delete(self, configid):
        api_action = self.namespace + 'delete'
        return self.request(api_action, locals())

    def list(self, nodebalancerid, configid=None):
        api_action = self.namespace + 'list'
        return self.request(api_action, locals())

    def update(self, configid, port=None, protocol=None, algorithm=None,
               stickiness=None, check=None, check_interval=None, check_timeout=None,
               check_attempts=None, check_path=None, check_body=None):
        api_action = self.namespace + 'update'
        return self.request(api_action, locals())


class Node(Base):
    namespace = 'node.'

    def create(self, configid, label, address, weight=None, mode=None):
        api_action = self.namespace + 'create'
        return self.request(api_action, locals())

    def delete(self, nodeid):
        api_action = self.namespace + 'delete'
        return self.request(api_action, locals())

    def list(self, configid, nodeid):
        api_action = self.namespace + 'list'
        return self.request(api_action, locals())

    def update(self, nodeid, label=None, address=None, weight=None, mode=None):
        api_action = self.namespace + 'update'
        return self.request(api_action, locals())


class Nodebalancer(Base):
    namespace = 'nodebalancer.'

    def __init__(self, api_key):
        super(Nodebalancer, self).__init__(api_key)
        self.config = Config(self.api_key, self.namespace)
        self.node = Node(self.api_key, self.namespace)

    def create(self, datacenterid, paymentterm):
        api_action = self.namespace + 'create'
        return self.request(api_action, locals())

    def delete(self, nodebalancerid):
        api_action = self.namespace + 'delete'
        return self.request(api_action, locals())

    def list(self, nodebalancerid=None):
        api_action = self.namespace + 'list'
        return self.request(api_action, locals())

    def update(self, nodebalancerid, label=None, clientconnthrottle=None):
        api_action = self.namespace + 'update'
        return self.request(api_action, locals())

