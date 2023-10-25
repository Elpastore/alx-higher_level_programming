#!/usr/bin/python3
"""Module of square"""


class Square:
    """
    This class represents a square.

    Attributes:
    - __size (int): The size of the square.
    - __position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square object with the specified size and position.

        Args:
        - size (int): The size of the square (default is 0).
        - position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
        - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
        - value (int): The size of the square.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
        - tuple: The position of the square as a tuple.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
        - value (tuple): The position of the square as a tuple.

        Raises:
        - TypeError: If value is not a tuple of two positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character.

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        DO the same as  my_print
        """
        my_list = []
        if self.__size == 0:
            return "\n"
        for _ in range(self.__position[1]):
            my_list.append("")
        for _ in range(self.__size):
            my_list.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(my_list)
