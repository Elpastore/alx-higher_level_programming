#!/usr/bin/python3
"""
module 1-my_list
"""


class MyList(list):
    """
    Class that inherite from list
    """
    def print_sorted(self):
        """
        method that print a list in sorted order
        """
        sorted_list = list(sorted(self))
        print(sorted_list)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
