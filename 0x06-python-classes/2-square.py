#!/usr/bin/python3
"""Module of square"""


class Square:
    """
    This class represents a square.

    Attributes:
    - __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initialization of the square.

        Args:
            - size (int): The size of the square.
        Raises:
            TypeError: check for type error
            ValueError: check if value is not negatif
        """

        if not isinstance(size, int):
            raise TypeError("size must be integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
