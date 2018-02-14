import sys

import pylogconf

from pytconf.config import register_main, config_arg_parse_and_launch, Config, \
    register_endpoint, create_int


class ConfigTotal(Config):
    """
    Parameters to select the total number of items to fetch
    """
    num = create_int(default=10, help_string="help for num")


@register_endpoint(
    configs=[
        ConfigTotal,
    ],
)
def command():
    # type: () -> None
    """
    This is help for command
    """
    print("num is {}".format(ConfigTotal.num))


@register_main()
def main():
    if sys.version_info[0] != 2:
        raise ValueError("only test this with python2")
    """
    This is a test
    """
    config_arg_parse_and_launch()


if __name__ == '__main__':
    main()
