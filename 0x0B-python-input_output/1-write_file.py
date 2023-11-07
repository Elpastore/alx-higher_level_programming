#!/usr/bin/python3
"""
1-write_file module
"""


def write_file(filename="", text=""):
    """
    function that write a string to a text
    and returns the number of characters
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
