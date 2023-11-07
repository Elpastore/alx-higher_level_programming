#!/usr/bin/python3
"""
3-to_json_string module
"""


def to_json_string(my_obj):
    """
    function that return the JSON representation of
    an object
    """
    import json
    return json.dumps(my_obj)
