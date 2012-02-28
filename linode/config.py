from .base import Base


class Config(Base):
    namespace = 'config.'

    def create(self, linode_id, kernel_id, label, comments='', ram_limit=0,
               disk_limit=',,,,,,,,', run_level='default', root_device_num=1,
               root_device_custom='', root_device_ro=True,
               helper_disable_update_db=True, helper_xen=True,
               helper_depmod=True, devtmpfs_automount=True):
        """
        Errors: NOTFOUND,VALIDATION
        """
        pass

    def delete(self, linode_id, config_id):
        """
        Errors: NOTFOUND,VALIDATION
        """
        pass

    def list(self, linode_id, config_id):
        """
        Errors: NOTFOUND
        """
        pass

    def update(self, linode_id, config_id, kernel_id, label, comments=None,
               ram_limit=None, disk_list=None, run_level=None, root_device_num=None,
               root_device_custom=None, root_device_ro=False,
               helper_disable_update_db=False, helper_xen=False, helper_depmod=False,
               devtmpfs_automount=False):
        """
        Errors: NOTFOUND,VALIDATION
        """
        pass

