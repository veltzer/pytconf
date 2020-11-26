import logging

from pytconf.data import LOGGER_NAME


def get_logger():
    return logging.getLogger(LOGGER_NAME)


def noun(name: str, num: int) -> str:
    """
    This function returns a noun in it's right for a specific quantity
    :param name:
    :param num:
    :return:
    """
    if num == 0 or num > 1:
        return name + "s"
    return name
