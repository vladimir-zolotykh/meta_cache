#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> f = Spam("foo")
Creating Spam(foo) ...
>>> g = Spam("bar")
Creating Spam(bar) ...
>>> h = Spam("foo")
>>> f is g
False
>>> f is h
True
"""


class Singleton(type):
    _instances = {}

    def __call__(self, *args, **kwars):
        if args not in self._instances:
            self._instances[args] = super().__call__(*args, **kwars)
        return self._instances[args]


class Spam(metaclass=Singleton):
    def __init__(self, name):
        print("Creating Spam({:s}) ...".format(name))
        self.name = name


if __name__ == "__main__":
    import doctest

    doctest.testmod()
