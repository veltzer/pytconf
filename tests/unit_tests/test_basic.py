"""
basic tests
"""

import unittest

import pytest

from pytconf import (
    Config,
    ParamCreator,
    config_arg_parse_and_launch,
    get_free_args,
)
from pytconf.config import FunctionData, get_pytconf


class ConfigTotal(Config):
    """
    Parameters to select the total number of items to fetch
    """

    num = ParamCreator.create_int(default=10, help_string="help for num")


def raise_value_error() -> None:
    """ function that raises an error """
    raise ValueError("raised on purpose")


class TestBasic(unittest.TestCase):
    """ all basic tests """
    def test_config_type(self) -> None:
        """ test that configurtion type is the right type """
        assert type(ConfigTotal.num) is int

    def test_config_value(self) -> None:
        """ test the value of the config option """
        assert ConfigTotal.num == 10

    def test_parsing(self) -> None:
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
        assert ConfigTotal.num == 30
        ConfigTotal.num = save

    def test_command_running(self) -> None:
        """ test that the right command is run """
        data = FunctionData(
            name="foo",
            description="foobar",
            function=raise_value_error,
            allow_free_args=True,
        )
        get_pytconf().register_function(data)
        with pytest.raises(ValueError, match="raised on purpose"):
            config_arg_parse_and_launch(args=["foo"])

    def test_free_args(self) -> None:
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
        assert get_free_args() == ["zoo"]
