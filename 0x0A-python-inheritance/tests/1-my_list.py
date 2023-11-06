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
        print (sorted(self))
