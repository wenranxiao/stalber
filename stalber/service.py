from oslo_config import cfg
from oslo_log import log as logging
from oslo_service import service
from oslo_utils import importutils

service_opts = [
    cfg.StrOpt('manager',
               default='stalber.manager.Manager',
               help='class'),
    cfg.StrOpt('host',
               default='host',
               help='Host name')]

CONF = cfg.CONF
CONF.register_opts(service_opts)


LOG = logging.getLogger(__name__)

class StalberService(service.Service):

    def __init__(self, host, binary, topic, manager,
                 periodic_enable=None, periodic_fuzzy_delay=None,
                 periodic_interval_max=None):

        super(StalberService, self).__init__()
        self.host = host
        self.manager_class_name = manager
        manager_class = importutils.import_class(self.manager_class_name)
        self.manager = manager_class(host=self.host)

    def start(self):
        LOG.info('stalberService Starting')

    def wait(self):
        pass

    def stop(self):
        pass

    def reset(self):
        logging.setup(cfg.CONF, 'foo')


    @classmethod
    def create(cls, host=None, binary=None, topic=None, manager=None):
        if not host:
            host=CONF.host
        if not binary:
            binary = os.path.basename(sys.argv[0])
        if not topic:
            topic = "stalber"
        if not manager:
            manager = CONF.manager
        service_obj = cls(host, binary, topic, manager)
        return service_obj

_launcher = None

def server(server, workers=None):
    global _launcher
    if _launcher:
        raise RuntimeError(_('serve() can only be called once'))
    _launcher = service.launch(CONF, server, workers=2,
                               restart_method='reload')

def wait():
    _launcher.wait()
