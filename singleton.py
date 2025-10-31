#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> s = Spam()
Creating Spam() ...
>>> f = Foo()
Creating Foo() ...
>>> s2 = Spam()
>>> s2 is s
True
"""


class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwars):
        if cls not in Singleton._instance:
            Singleton._instance[cls] = super().__call__(*args, **kwars)
        return Singleton._instance[cls]


class Spam(metaclass=Singleton):
    def __init__(self):
        print("Creating Spam() ...")


class Foo(metaclass=Singleton):
    def __init__(self):
        print("Creating Foo() ...")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
