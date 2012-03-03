from .base import Base


class Stackscript(Base):
    namespace = 'stackscript.'

    def create(self, label, distributionidlist, script, description=None,
               ispublic=None, rev_not=None):
        api_action = self.namespace + 'create'
        return self.request(api_action, locals())

    def delete(self, stackscriptid):
        api_action = self.namespace + 'delete'
        return self.request(api_action, locals())

    def list(self, stackscriptid=None):
        api_action = self.namespace + 'list'
        return self.request(api_action, locals())

    def update(self, stackscriptid, label=None, description=None,
               distributionidlist=None, ispublic=None, rev_note=None, script=None):
        api_action = self.namespace + 'update'
        return self.request(api_action, locals())

