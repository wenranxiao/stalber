from oslo_config import cfg
from oslo_log import log as logging
from oslo_service import periodic_task


LOG = logging.getLogger(__name__)
CONF = cfg.CONF


class Manager(periodic_task.PeriodicTasks):

    def __init__(self, host=None, service_name='stalber'):
        LOG.info("Manager init")
        super(Manager, self).__init__(CONF)


    def periodic_tasks(self, context, raise_on_error=False):
        """Tasks to be run at a periodic interval."""
        return self.run_periodic_tasks(context, raise_on_error=raise_on_error)

    @periodic_task.periodic_task(spacing=1, run_immediately=True)
    def do_print(self, context):
        LOG.info('print cccc')
