from .base import Base


class Ip(Base):
    namespace = 'ip.'

    def addprivate(self, linode_id):
        pass

    def list(self, linode_id, ip_address_id=None):
        pass

