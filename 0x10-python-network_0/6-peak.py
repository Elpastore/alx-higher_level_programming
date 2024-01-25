#!/usr/bin/python3
"""Interview question"""


def find_peak(list_of_integers):
    """
     finds a peak in a list of unsorted integers.
    """
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
