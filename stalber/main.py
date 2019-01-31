import eventlet
import sys

from oslo_config import cfg
from oslo_log import log as logging

from stalber import config
from stalber import service


CONF = cfg.CONF
LOG = logging.getLogger(__name__)


def main():
    config.parse_args(sys.argv)
    logging.setup(CONF, "stabler")
    eventlet.monkey_patch()
    server = service.StalberService.create(binary='stabler', topic='stabler')
    service.server(server)
    service.wait()

if __name__ == "__main__":
    main()
