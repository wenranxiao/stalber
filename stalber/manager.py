from oslo_log import log as logging


LOG = logging.getLogger(__name__)
class Manager(object):
    def __init__(self, host=None, service_name='stalber'):
        LOG.info("Manager init")
        pass

