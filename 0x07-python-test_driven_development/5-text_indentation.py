#!/usr/bin/python3
"""
5-text_indentation module
"""


def text_indentation(text):
    """
    Function that print text
    Args:
        -text (str): text to be printed
    Raises:
        -TypeError: check for string
    """
    if not isinstance(text, str):
        raise TypeError("ext must be a string")

    result = ""
    for i in text:
        if i in ['.', '?', ':']:
            result += i
            result += "\n\n"
        else:
            result += i
    print(result.strip())
