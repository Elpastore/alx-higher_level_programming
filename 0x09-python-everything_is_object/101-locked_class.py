#!/usr/bin/python3
"""
Locked module
"""


class LockedClass:
    """
    Class that restrict the dynamically creating
    instance with certain condition
    """
    __slots__ = ["fist_name"]
