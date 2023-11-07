#!/usr/bin/python3
"""
6-load_from_json_file module
"""


def load_from_json_file(filename):
    """
    function that creates an object from JSON
    """
    import json

    with open(filename, "r") as file:
        data = json.load(file)
    return data
