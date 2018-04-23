import sys
import unittest

from pytconf.config import register_main, config_arg_parse_and_launch, Config, \
    register_endpoint, ParamCreator


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
def command():
    # type: () -> None
    """
    This is help for command
    """
    print("num is {}".format(ConfigTotal.num))


@register_main()
def main():
    """
        This is a test
    """
    sys.argv += ["--num=30"]
    print(sys.argv)
    config_arg_parse_and_launch()


class TestBasic(unittest.TestCase):
    def testType(self):
        self.assertEquals(type(ConfigTotal.num), int)

    def testValue(self):
        self.assertEquals(ConfigTotal.num, 10)
