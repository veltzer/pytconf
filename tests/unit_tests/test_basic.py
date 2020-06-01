import unittest

from pytconf.config import config_arg_parse_and_launch, \
    Config, ParamCreator, register_function, get_free_args


class ConfigTotal(Config):
    """
    Parameters to select the total number of items to fetch
    """
    num = ParamCreator.create_int(default=10, help_string="help for num")


def raise_value_error() -> None:
    raise ValueError()


class TestBasic(unittest.TestCase):
    # def setUp(self) -> None:
    #    logger = logging.getLogger("pytconf")
    #    logger.setLevel(logging.DEBUG)

    def test_config_type(self):
        self.assertEqual(type(ConfigTotal.num), int)

    def test_config_value(self):
        self.assertEqual(ConfigTotal.num, 10)

    def test_parsing(self):
        save = ConfigTotal.num
        config_arg_parse_and_launch(launch=False, args=["foo", "--num=30"])
        self.assertEqual(ConfigTotal.num, 30)
        ConfigTotal.num = save

    def test_command_running(self):
        register_function(raise_value_error)
        with self.assertRaises(ValueError):
            config_arg_parse_and_launch(args=["foo", "raise_value_error"])

    def test_free_args(self):
        config_arg_parse_and_launch(launch=False, args=["foo", "bar", "--num=30", "zoo"])
        self.assertListEqual(get_free_args(), ["zoo"])
