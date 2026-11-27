"""
helpers to print stuff in color
"""


import os

from termcolor import colored, cprint


def print_highlight(text: str) -> None:
    cprint(text=text, color="white", attrs=["bold"])


def print_warn(text: str) -> None:
    cprint(text=text, color="red", attrs=["bold"])


def print_error(text: str) -> None:
    cprint(text=text, color="red", attrs=["bold"])


def print_title(text: str) -> None:
    cprint(text=text, color="green", attrs=[])


def color_hi(text: str) -> str:
    return colored(text=text, color="white", attrs=["bold"])


def color_warn(text: str) -> str:
    return colored(text=text, color="red", attrs=["bold"])


def color_ok(text: str) -> str:
    return colored(text=text, color="green", attrs=["bold"])


def identity(text: str):
    return text


color = "PYTCONF_DISABLE_COLORS" not in os.environ


if not color:
    print_highlight = print
    print_warn = print
    print_error = print
    print_title = print
    color_hi = identity
    color_warm = identity
    color_ok = identity
