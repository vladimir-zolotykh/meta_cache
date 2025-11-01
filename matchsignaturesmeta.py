#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from inspect import signature, Parameter
import logging

logging.basicConfig(level=logging.INFO)


def signatures_equal(sig1, sig2):
    params1 = list(sig1.parameters.values())
    params2 = list(sig2.parameters.values())

    if len(params1) != len(params2):
        return False

    for p1, p2 in zip(params1, params2):
        # Compare only kind and default, not name
        if p1.kind != p2.kind or (
            p1.default != p2.default
            and not (p1.default is Parameter.empty and p2.default is Parameter.empty)
        ):
            return False
    if sig1.return_annotation != sig2.return_annotation:
        if not (sig1.return_annotation is sig2.return_annotation is Parameter.empty):
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
                    "Signature mismatch for %r. %s != %s", meth.__name__, sig, sig_prev
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
