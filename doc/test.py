#!/usr/bin/env python

"""
This is the essence of how pytconf works and how it is now designed
"""

d = {}

global_list: list[int] = []


class Meta(type):
    def __new__(cls, name, bases, namespace):
        # pylint: disable=global-statement
        global global_list
        ret = super().__new__(cls, name, bases, namespace)
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
        # global global_list
        global_list.append(extra)
        return default


class B(Config):
    var_a: int = Config.create_int(5, 34)
    var_b: int = Config.create_int(6, 35)


class C(Config):
    zoo: int = Config.create_int(7, 36)
    koo: int = Config.create_int(8, 37)


assert B.var_a == 5
assert B.var_b == 6
assert C.zoo == 7
assert C.koo == 8
assert d[(B, "var_a")] == 34
assert d[(B, "var_b")] == 35
assert d[(C, "zoo")] == 36
assert d[(C, "koo")] == 37
