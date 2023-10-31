#!/usr/bin/python3
"""
    Module 0-add_integer for calculation

    Method add_integer: compute the sum
"""


def add_integer(a, b=98):
    """
    Returns: The sum of two value(int)
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Values should be integer or float")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
