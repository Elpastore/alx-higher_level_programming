#!/usr/bin/python3
"""
100-my_int module
"""


class MyInt(int):
    """
    Class that inherits from int
    """
    def __eq__(self, value):
        """
        method that inverted ==
        """
        return not super().__eq__(value)

    def __ne__(self, value):
        """
        method that inverted !=
        """
        return not super().__ne__(value)
