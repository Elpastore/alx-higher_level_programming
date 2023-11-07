#!/usr/bin/python3
"""
2-append_write module
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end
    of a text file(UTF8) and return the number of character
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
