from .base import Base


class Resource(Base):
    namespace = 'resource.'

    def create(self, domain_id, type, name='', target='', priority=10, weight=5,
               port=80, protocol='udp', ttl_sec=0):
        """
        Errors: NOACCESS,VALIDATION
        """
        pass

    def delete(self, domain_id, resource_id):
        """
        Errors: NOTFOUND
        """
        pass

    def list(self, domain_id, resource_id=None):
        api_action = self.namespace + 'list'
        return self.request(api_action, locals())

    def update(self, domain_id, resource_id, name=None, target=None, priority=None,
               weight=None, port=None, protocol=None, ttl_sec=None):
        """
        Errors: NOTFOUND,VALIDATION
        """
        pass


class Domain(Base):
    namespace = 'domain.'

    def __init__(self, api_key):
        super(Domain, self).__init__(api_key)
        self.resource = Resource(self.api_key, self.namespace)

    def create(self, domain, type, soa_email, description='', refresh_sec=0,
               retry_sec=0, expire_sec=0, ttl_sec=0, status=1, master_ips=''):
        """
        Errors: NOACCESS,VALIDATION
        """
        pass

    def delete(self, domain_id):
        """
        Errors: NOTFOUND
        """
        pass

    def list(self, domain_id=None):
        api_action = self.namespace + 'list'
        return self.request(api_action, locals())

    def update(self, domain_id, domain=None, description=None, type=None,
               soa_email=None, refresh_sec=None, retry_sec=None, expire_sec=None,
               ttl_sec=None, status=None, master_ips=None):
        pass

