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
        raise TypeError("text must be a string")

    flag = 0
    for char in text:
        if flag == 0:
            if char == " ":
                continue
            else:
                flag = 1
        if flag == 1:
            if char in ["?", ".", ":"]:
                print(char)
                print()
                flag = 0
            else:
                print(char, end="")
