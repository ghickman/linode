from .base import Base
from .config import Config
from .ip import Ip


class Linode(Base):
    namespace = 'linode.'

    def __init__(self, api_key):
        super(Linode, self).__init__(api_key)
        self.ip = Ip(self.api_key, self.namespace)
        self.config = Config(self.api_key, self.namespace)

    # TODO: learn decorators
    # @payment_term
    def boot(self, datacenter_id, plan_id, payment_term):
        """
        Errors: NOACCESS,CCFAILED,VALIDATION
        """
        pass

    def create(self, datacenter_id, plan_id, payment_term):
        """
        Errors: NOACCESS,CCFAILED,VALIDATION
        """
        pass

    def delete(self, linode_id, skip_checks=False):
        """
        Errors: NOTFOUND,LINODENOTEMPTY
        """
        pass

    def list(self, linode_id=None):
        api_action = self.namespace + 'list'
        r = self.request(api_action)
        print r.status_code
        print r.content

    def reboot(self, linode_id, config_id=None):
        """
        Errors: NOTFOUND
        """
        pass

    def resize(self, linode_id, plan_id):
        """
        Errors: NOTFOUND,CCFAILED,VALIDATION
        """
        pass

    def shutdown(self, linode_id, plan_id):
        """
        Errors: NOTFOUND
        """
        pass

    def update(linode_id, label, lpm_display_group=None,
               alert_cpu_enabled=False, alert_cpu_threshold=None,
               alert_diskio_enabled=False, alert_diskio_threshold=None,
               alert_bwin_enabled=False, alert_bwin_threshold=None,
               alert_bwout_enabled=False, alert_bwout_threshold=None,
               alert_bwquota_enabled=False, alert_bwquota_threshold=None,
               backup_window=None, backup_weekly_day=None, watchdog=False):
        # TODO: Check the defaults for all of these. Might be easier to default to None and not include.
        """
        Errors: NOTFOUND,VALIDATION
        """
        pass

