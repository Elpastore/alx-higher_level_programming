#!/usr/bin/python3
"""Interview question"""


def find_peak(list_of_integers):
    """
     finds a peak in a list of unsorted integers.
    """
    if list_of_integers:
        sorted_list = sorted(list_of_integers)
        return sorted_list[-1]
