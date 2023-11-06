#!/usr/bin/python3
""" 
Module 1-my_list 
"""


class MyList(list):
    """ 
    Class of MyList
    """

    def print_sorted(self):
        """
        print sorted list
        """
        print(sorted(list(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
