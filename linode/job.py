from .base import Base


class Job(Base):
    namespace = 'job.'

    def list(self, linode_id, job_id=None, pending_only=False):
        pass

