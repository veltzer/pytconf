import pylogconf.core

from modules.data_vault.lib.pyconf.config import register_main, config_arg_parse_and_launch, Config, \
    register_cli, create_int


class ConfigTotal(Config):
    """
    Parameters to select the total number of items to fetch
    """
    num = create_int(default=10, help="help for num")


@register_cli(
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
    """
    Data Vault is your way to get data in Twiggle.
    Author: Mark Veltzer <mark@twiggle.com>
    """
    pylogconf.core.setup()
    config_arg_parse_and_launch()


if __name__ == '__main__':
    main()
