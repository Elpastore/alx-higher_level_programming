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
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieve the size's square

        Returns:
            -int:  the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set the size's square

        Args:
            - value (int): value to be set
        Raises:
            -TypeError: Check for integer value
            -ValueError: Check for negatif integer
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        method of class Square that return current the square
        Returns:
            the square area
        """
        return self.__size ** 2
