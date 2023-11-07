#!/usr/bin/python3
"""
4-from_json_string module
"""


def from_json_string(my_str):
    """
    function that convert JSOn rep to a python object
    Args:
        -my_str: python object
    return:
        the python object
    """
    import json
    return json.loads(my_str)
