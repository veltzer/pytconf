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

class A(object, metaclass=Meta):
    @classmethod
    def ParamCreatorInt(cls: ClassVar, default: int, extra:int) -> int:
        global glist
        glist.append(extra)
        return default


class B(A):
    foo: int=A.ParamCreatorInt(5, 34)
    bar: int=A.ParamCreatorInt(6, 35)

class C(A):
    zoo: int=A.ParamCreatorInt(7, 36)
    koo: int=A.ParamCreatorInt(8, 37)


assert(B.foo==5)
assert(B.bar==6)
assert(C.zoo==7)
assert(C.koo==8)
print(d)
