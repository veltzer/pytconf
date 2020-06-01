import logging
import unittest

from pytconf.config import config_arg_parse_and_launch, \
    register_function

g: int = 3


def command() -> None:
    """
    This is help for command
    """
    global g
    g = 7


class TestMinimal(unittest.TestCase):
    def setUp(self) -> None:
        logger = logging.getLogger("pytconf")
        logger.setLevel(logging.DEBUG)

    def test_command_running(self):
        register_function(
            command,
        )
        global g
        g = 5
        config_arg_parse_and_launch(args=["foo", "command"])
        self.assertEqual(g, 7)
