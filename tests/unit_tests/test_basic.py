"""
basic tests
"""

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
    """ function that raises an error """
    raise ValueError()


class TestBasic(unittest.TestCase):
    """ all basic tests """
    def test_config_type(self):
        """ test that configurtion type is the right type """
        self.assertEqual(type(ConfigTotal.num), int)

    def test_config_value(self):
        """ test the value of the config option """
        self.assertEqual(ConfigTotal.num, 10)

    def test_parsing(self):
        """ test command line parser """
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
        """ test that the right command is run """
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
        """ test correct free argument parsing """
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
