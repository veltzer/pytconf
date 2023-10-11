import unittest
from pytconf.config import FunctionData, get_pytconf

from pytconf import (
    config_arg_parse_and_launch,
    Config,
    get_free_args,
    ParamCreator,
)


class ConfigTotal(Config):
    """
    Parameters to select the total number of items to fetch
    """

    num = ParamCreator.create_int(default=10, help_string="help for num")


def raise_value_error() -> None:
    raise ValueError()


class TestBasic(unittest.TestCase):
    def test_config_type(self):
        self.assertEqual(type(ConfigTotal.num), int)

    def test_config_value(self):
        self.assertEqual(ConfigTotal.num, 10)

    def test_parsing(self):
        save = ConfigTotal.num
        data = FunctionData(
            name="foo",
            description="foobar",
            function=raise_value_error,
        )
        get_pytconf().register_function(data)
        config_arg_parse_and_launch(
            args=["foo", "--num=30"],
            launch=False,
            do_exit=False,
        )
        self.assertEqual(ConfigTotal.num, 30)
        ConfigTotal.num = save

    def test_command_running(self):
        data = FunctionData(
            name="foo",
            description="foobar",
            function=raise_value_error,
            allow_free_args=True,
        )
        get_pytconf().register_function(data)
        with self.assertRaises(ValueError):
            config_arg_parse_and_launch(args=["foo"])

    def test_free_args(self):
        data = FunctionData(
            name="foo",
            description="foobar",
            function=raise_value_error,
            allow_free_args=True,
        )
        get_pytconf().register_function(data)
        config_arg_parse_and_launch(
            args=["foo", "--num=30", "zoo"],
            launch=False,
            do_exit=False,
        )
        self.assertListEqual(get_free_args(), ["zoo"])
