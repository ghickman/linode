from .base import Base


class Config(Base):
    namespace = 'config.'

    def create(self, linodeid, kernelid, label, comments=None, ramlimit=None,
               disklimit=None, runlevel=None, rootdevicenum=None,
               rootdevicecustom=None, rootdevicero=None,
               helper_disableupdatedb=None, helper_xen=None,
               helper_depmod=None, devtmpfs_automount=None):
        api_action = self.namespace + 'create'
        return self.request(api_action, locals())

    def delete(self, linodeid, configid):
        api_action = self.namespace + 'delete'
        return self.request(api_action, locals())

    def list(self, linodeid, configid):
        api_action = self.namespace + 'list'
        return self.request(api_action, locals())

    def update(self, linodeid, configid, kernelid, label, comments=None,
               ramlimit=None, disklist=None, runlevel=None, rootdevicenum=None,
               rootdevicecustom=None, rootdevicero=None,
               helper_disableupdatedb=None, helper_xen=None, helper_depmod=None,
               devtmpfs_automount=None):
        api_action = self.namespace + 'update'
        return self.request(api_action, locals())


class Disk(Base):
    namespace = 'disk.'

    def create(self, linodeid, label, type, size, isreadonly=None,
               stackscriptrevid=None, stackscriptudf_json=None):
        api_action = self.namespace + 'create'
        return self.request(api_action, locals())

    def createfromdistribution(self, linodeid, distributionid, label, size,
                               rootpass=None, rootsshkey=None):
        api_action = self.namespace + 'createfromdistribution'
        return self.request(api_action, locals())

    def createfromstackscript(self, linodeid, stackscriptid, stackscriptudfresponses,
                              distributionid, label, size, rootpass):
        api_action = self.namespace + 'createfromstackscript'
        return self.request(api_action, locals())

    def delete(self, linodeid, diskid):
        api_action = self.namespace + 'delete'
        return self.request(api_action, locals())

    def duplicate(self, linodeid, diskid):
        api_action = self.namespace + 'duplicate'
        return self.request(api_action, locals())

    def list(self, linodeid, diskid=None):
        api_action = self.namespace + 'list'
        return self.request(api_action, locals())

    def resize(self, linodeid, diskid, size):
        api_action = self.namespace + 'resize'
        return self.request(api_action, locals())

    def update(self, linodeid, diskid, label=None, isreadonly=None):
        api_action = self.namespace + 'update'
        return self.request(api_action, locals())


class Ip(Base):
    namespace = 'ip.'

    def addprivate(self, linodeid):
        api_action = self.namespace + 'addprivate'
        return self.request(api_action, locals())

    def list(self, linodeid, ipaddressid=None):
        api_action = self.namespace + 'list'
        return self.request(api_action, locals())


class Job(Base):
    namespace = 'job.'

    def list(self, linodeid, jobid=None, pendingonly=None):
        api_action = self.namespace + 'list'
        return self.request(api_action, locals())


class Linode(Base):
    namespace = 'linode.'

    def __init__(self, api_key):
        super(Linode, self).__init__(api_key)
        self.config = Config(self.api_key, self.namespace)
        self.disk = Disk(self.api_key, self.namespace)
        self.ip = Ip(self.api_key, self.namespace)
        self.job = Job(self.api_key, self.namespace)

    def boot(self, linodeid, confidid):
        api_action = self.namespace + 'boot'
        return self.request(api_action, locals())

    def create(self, datacenterid, planid, paymentterm):
        api_action = self.namespace + 'create'
        return self.request(api_action, locals())

    def delete(self, linodeid, skipchecks=None):
        api_action = self.namespace + 'delete'
        return self.request(api_action, locals())

    def list(self, linodeid=None):
        api_action = self.namespace + 'list'
        return self.request(api_action, locals())

    def reboot(self, linodeid, configid=None):
        api_action = self.namespace + 'reboot'
        return self.request(api_action, locals())

    def resize(self, linodeid, planid):
        api_action = self.namespace + 'resize'
        return self.request(api_action, locals())

    def shutdown(self, linodeid):
        api_action = self.namespace + 'shutdown'
        return self.request(api_action, locals())

    def update(self, linodeid, label, lpm_displaygroup=None,
               alert_cpu_enabled=None, alert_cpu_threshold=None,
               alert_diskio_enabled=None, alert_diskio_threshold=None,
               alert_bwin_enabled=None, alert_bwin_threshold=None,
               alert_bwout_enabled=None, alert_bwout_threshold=None,
               alert_bwquota_enabled=None, alert_bwquota_threshold=None,
               backupwindow=None, backupweeklyday=None, watchdog=None):
        api_action = self.namespace + 'update'
        return self.request(api_action, locals())

