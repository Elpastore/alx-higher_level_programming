#!/usr/bin/python3
"""
5-save_to_json_file module
"""


def save_to_json_file(my_obj, filename):
    """
    function that write object to a text file
    """
    import json

    with open(filename, "w") as file:
        json.dump(my_obj, file)
