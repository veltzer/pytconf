import sys
import unittest

from pytconf.config import register_main, config_arg_parse_and_launch,\
    Config, register_endpoint, ParamCreator


class ConfigTotal(Config):
    """
    Parameters to select the total number of items to fetch
    """
    num = ParamCreator.create_int(default=10, help_string="help for num")


@register_endpoint(
    configs=[
        ConfigTotal,
    ],
)
def command() -> None:
    """
    This is help for command
    """
    print("num is {}".format(ConfigTotal.num))


@register_main()
def main():
    """
        This is a test
    """

    print(sys.argv)
    config_arg_parse_and_launch()


class TestBasic(unittest.TestCase):
    def test_type(self):
        self.assertEqual(type(ConfigTotal.num), int)

    def test_value(self):
        self.assertEqual(ConfigTotal.num, 10)

    def test_parsing(self):
        sys.argv += ["--num=30"]
        save = ConfigTotal.num
        config_arg_parse_and_launch(launch=False, print_messages=False)
        self.assertEqual(ConfigTotal.num, 30)
        ConfigTotal.num = save
