#!/usr/bin/python3

"""
This is the essence of how pytconf works and how it is now designed
"""

from typing import List

d = {}

global_list: List[int] = []


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        global global_list
        ret = super().__new__(mcs, name, bases, namespace)
        i = 0
        for k, v in namespace.items():
            if not k.startswith("__") and not isinstance(v, classmethod):
                d[(ret, k)] = global_list[i]
                i += 1
        global_list = []
        return ret


class Config(metaclass=Meta):
    @classmethod
    def create_int(cls, default: int, extra: int) -> int:
        global global_list
        global_list.append(extra)
        return default


class B(Config):
    foo: int = Config.create_int(5, 34)
    bar: int = Config.create_int(6, 35)


class C(Config):
    zoo: int = Config.create_int(7, 36)
    koo: int = Config.create_int(8, 37)


assert (B.foo == 5)
assert (B.bar == 6)
assert (C.zoo == 7)
assert (C.koo == 8)
assert (d[(B, "foo")] == 34)
assert (d[(B, "bar")] == 35)
assert (d[(C, "zoo")] == 36)
assert (d[(C, "koo")] == 37)
