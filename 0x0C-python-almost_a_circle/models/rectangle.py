#!/usr/bin/python3
"""
models/rectangle module
"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization of the class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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

    @property
    def x(self):
        """
        Retrieve the x of the rectangle
        Returns:
            -int: the x of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        set the value of the x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        Retrieve the y of the rectangle
        Returns:
            -int: the y of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        set the value of the y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Method that give the area of rectangle
        Returns:
            -int : the area
        """
        return self.__height * self.__width

    def display(self):
        """
        method that display  the rectangle
        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """
        method that assigns an argument to each attribute
        """
        key = ["id", "width", "height", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, key[i], arg)
        if kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        return the dictionary representaion of a Rectangle
        """
        dictionary = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
        return dictionary

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
