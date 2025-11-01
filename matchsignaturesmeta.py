#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from inspect import signature, Signature
import logging

logging.basicConfig(level=logging.INFO)


def signatures_equal(sig1: Signature, sig2: Signature) -> bool:
    params1 = list(sig1.parameters.values())
    params2 = list(sig2.parameters.values())

    if len(params1) != len(params2):
        return False

    for p1, p2 in zip(params1, params2):
        temp_name = "temp"
        p1_normalized = p1.replace(name=temp_name)
        p2_normalized = p2.replace(name=temp_name)
        if p1_normalized != p2_normalized:
            return False
    return True


class MatchSignaturesMeta(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        sup = super(self, self)
        for name, meth in clsdict.items():
            if name.startswith("_") or not callable(meth):
                continue
            meth_prev = getattr(sup, name, None)
            if meth_prev is None:
                continue
            sig = signature(meth)
            sig_prev = signature(meth_prev)
            if sig == sig_prev:
                continue
            if not signatures_equal(sig, sig_prev):
                logging.warning(
                    "Signature mismatch for %r. %s != %s",
                    meth.__qualname__,
                    sig,
                    sig_prev,
                )


# Example
class Root(metaclass=MatchSignaturesMeta):
    pass


class A(Root):
    def foo(self, x, y):
        pass

    def spam(self, x, *, z):
        pass


# Class with redefined methods, but slightly different signatures
class B(A):
    def foo(self, a, b):
        pass

    def spam(self, x, z):
        pass
