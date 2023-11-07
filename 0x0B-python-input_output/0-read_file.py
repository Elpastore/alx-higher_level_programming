#!/usr/bin/python3
"""
0-read_file module
"""


def read_file(filename=""):
    """
    function that read a text file
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
