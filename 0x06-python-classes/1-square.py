#!/usr/bin/python3
class Square:
    """
    This class represents a square

    Attributes:
    -__size (int):  the size of the square as private
    Methods:
    -__init__: Constructor that start by given a value of square

    """
    def __init__(self, size):
        """
        Iniatialisation of the square

        Args:
            -size (int): the size of the square
        """
        self.__size = size
