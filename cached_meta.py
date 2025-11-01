#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
Cache instances of classes
"""
import weakref

# from collections import defaultdict


class Cached(type):
    def __init__(cls, clsname, basis, clsdict):
        super().__init__(clsname, basis, clsdict)
        cls._cache = weakref.WeakValueDictionary()

    def __call__(cls, *args, **kwargs):
        if args not in cls._cache:
            instance = super().__call__(*args, **kwargs)
            cls._cache[args] = instance
        return cls._cache[args]


class Person(metaclass=Cached):
    def __init__(self, name, age):
        print(f"Creating Person() for {name!r}")
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person({self.name!r}, {self.age})"


if __name__ == "__main__":
    arthur = Person("Arthur Davies", 63)
    print(arthur)
    oliver = Person("Oliver Thompson", 35)
    arthur = Person("Arthur Davies", 63)
    arthur = Person("Arthur Davies", 64)
