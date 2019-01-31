from oslo_config import cfg
from oslo_log import log

CONF = cfg.CONF

def parse_args(argv, default_config_files = None):
    log.register_options(CONF)
    #rpc.set_defaults(control_exchange='hagent')
    CONF(argv[1:], project='hagent', version='0.1', default_config_files=default_config_files)
    #rpc.init(CONF)
