#!/usr/bin/python3

from typing import List, Union
from registry import the_registry
from param_collector import the_collector


class MetaConfig(type):
    """
    Meta class for all configs
    """

    def __new__(mcs, name, bases, namespace):
        ret = super().__new__(mcs, name, bases, namespace)
        i = 0
        for k, v in namespace.items():
            if not k.startswith("__") and not isinstance(v, classmethod):
                the_registry.register(ret, k, the_collector.get_item(i))
                i += 1
        the_collector.clear()
        return ret


class Config(metaclass=MetaConfig):
    """
    Base class for all configs
    """


class Unique:
    pass


NO_DEFAULT = Unique()


def create_list_int(
    default: Union[List[int], Unique] = NO_DEFAULT,
) -> List[int]:
    assert isinstance(default, List)
    return default


class Foobar(Config):
    columns = create_list_int()


for x in Foobar.columns:
    print(x)
