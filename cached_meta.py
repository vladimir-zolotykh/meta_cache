#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
Cache instances of classes
"""


class Cached(type):
    _cache = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._cache:
            cls._cache[cls] = {}
        if args not in cls._cache[cls]:
            cls._cache[cls][args] = super().__call__(*args, **kwargs)
        return cls._cache[cls][args]


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
