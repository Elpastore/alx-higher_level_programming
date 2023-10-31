#!/usr/bin/python3
"""
The 4-print_square module
"""


def print_square(size):
    """
    Function that prints a square with the character
    Args:
        -size (int): length of the square
    Raises:
        -ValueError: check the size value
        -TypeError: check the size value and type
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
