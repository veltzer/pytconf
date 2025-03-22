""" initialization of the condif module """

from pytconf.param import ParamCreator  # noqa F401
from pytconf.config import (  # noqa F401
    Config,
    register_main,
    config_arg_parse_and_launch,
    register_endpoint,
    register_function,
    get_free_args,
    write_config_file,
    write_config,
    rm_config_file,
)
