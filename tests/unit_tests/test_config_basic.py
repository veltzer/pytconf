import logging
import unittest

from pytconf.config import config_arg_parse_and_launch, \
    Config, register_endpoint, ParamCreator, register_function


class ConfigTotal(Config):
    """
    Parameters to select the total number of items to fetch
    """
    num = ParamCreator.create_int(default=10, help_string="help for num")


def command() -> None:
    """
    This is help for command
    """
    print("num is {}".format(ConfigTotal.num))


class TestBasic(unittest.TestCase):
    def setUp(self) -> None:
        logger = logging.getLogger("pytconf")
        logger.setLevel(logging.DEBUG)

    def test_type(self):
        self.assertEqual(type(ConfigTotal.num), int)

    def test_value(self):
        self.assertEqual(ConfigTotal.num, 10)

    def test_parsing(self):
        register_function(
            command,
            configs=[ConfigTotal],
        )
        save = ConfigTotal.num
        config_arg_parse_and_launch(launch=False, print_messages=False, args=["foo", "--num=30"])
        self.assertEqual(ConfigTotal.num, 30)
        ConfigTotal.num = save
