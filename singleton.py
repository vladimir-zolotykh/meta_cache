#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class Singleton(type):
    _instances = {}

    def __call__(self, *args, **kwars):
        if args in self._instances:
            inst = self._instances[args]
        else:
            inst = super().__call__(*args, **kwars)
            self._instances[args] = inst
        return inst


class Spam(metaclass=Singleton):
    def __init__(self, name):
        print("Creating Spam({:s}) ...".format(name))
        self.name = name


if __name__ == "__main__":
    f = Spam("foo")
    g = Spam("bar")
    h = Spam("foo")
    print("f is g: ", f is g)
    print("f is h: ", f is h)
