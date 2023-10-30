#!/usr/bin/python3
"""
1-rectangle module
"""


class Rectangle:
    """
    Class that define an empty rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialization of the class
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve the width of the rectangle
        Returns:
            -int: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the value of the width
        Args:
            -value (int): value to set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle
        Returns:
            -int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the value of the heigth
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
