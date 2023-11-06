#!/usr/bin/python3
"""
4-inherits_from module
"""


def inherits_from(obj, a_class):
    """
    function that check for instance of an object
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
