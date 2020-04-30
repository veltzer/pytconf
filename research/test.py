#!/usr/bin/python3

from typing import ClassVar

d = {}

glist = []

class Meta(type):
    def __new__(mcs, name, bases, namespace):
        global glist
        ret=super().__new__(mcs, name, bases, namespace)
        i=0
        for k,v in namespace.items():
            if not k.startswith("__") and not isinstance(v, classmethod):
                d[(ret, k)]=glist[i]
                i+=1
        glist=[]
        return ret

class Config(object, metaclass=Meta):
    @classmethod
    def create_int(cls: ClassVar, default: int, extra:int) -> int:
        global glist
        glist.append(extra)
        return default


class B(Config):
    foo: int=Config.create_int(5, 34)
    bar: int=Config.create_int(6, 35)

class C(Config):
    zoo: int=Config.create_int(7, 36)
    koo: int=Config.create_int(8, 37)


assert(B.foo==5)
assert(B.bar==6)
assert(C.zoo==7)
assert(C.koo==8)
assert(d[(B,"foo")]==34)
assert(d[(B,"bar")]==35)
assert(d[(C,"zoo")]==36)
assert(d[(C,"koo")]==37)
