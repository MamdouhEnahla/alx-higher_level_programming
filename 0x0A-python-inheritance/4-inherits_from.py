#!/usr/bin/python3
"""
the inherits_from function
"""


def inherits_from(obj, a_class):
    """returns true if obj is a subclass, otherwise false"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
