from __future__ import print_function

from enum import Enum

from typing import List, Type


def enum_type_to_list_str(e):
    # type: (Type[Enum]) -> List[str]
    a = [x.name for x in e]
    return a


def enum_value_to_str(ev):
    # type: (Type[Enum]) -> str
    return ev.name


def str_to_enum_value(s, e):
    # type: (str, Type[Enum]) -> Type[Enum]
    for x in e:
        if s == x.name:
            return x
    raise ValueError("cannot find value [{}]".format(s))


def str_to_enum_int(s, e):
    # type: (str, Type[Enum]) -> int
    for x in e:
        if s == x.name:
            return x.value
    raise ValueError("cannot find value [{}]".format(s))


def enum_int_to_name(i, e):
    # type: (int, Type[Enum]) -> str
    for x in e:
        if i == x.value:
            return x.name
    raise ValueError("cannot find value [{}]".format(i))


def list_of_names_to_multi_enum_value(s, e):
    # type: (str, Type[Enum]) -> int
    sum_all = 0
    if s == "":
        return sum_all
    for name in s.split(','):
        sum_all += pow(2, str_to_enum_int(name, e))
    return sum_all


def multi_enum_value_to_list_of_names(t, e):
    # type: (int, Type[Enum]) -> str
    max_value = max(x.value for x in e)
    results = []
    while max_value > 0:
        if t > pow(2, max_value):
            t -= pow(2, max_value)
            value_str = enum_int_to_name(max_value, e)
            max_value -= 1
            results.append(value_str)
    return ",".join(results)
