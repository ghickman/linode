from .base import Base


class Account(Base):
    namespace = 'account.'

    def info(self):
        api_action = self.namespace + 'info'
        return self.request(api_action, locals())


class Avail(Base):
    namespace = 'avail.'

    def linodeplans(self, plan_id=None):
        api_action = self.namespace + 'linodeplans'
        return self.request(api_action, locals())

    def datacenters(self):
        api_action = self.namespace + 'datacenters'
        return self.request(api_action, locals())

    def distributions(self, distribution_id=None):
        api_action = self.namespace + 'distributions'
        return self.request(api_action, locals())

    def kernels(self, kernel_id=None, is_xen=False):
        api_action = self.namespace + 'kernels'
        return self.request(api_action, locals())

    def stackscripts(self, distribution_id=None, distribution_vendor=None,
                     keywords=None):
        api_action = self.namespace + 'stackscripts'
        return self.request(api_action, locals())

