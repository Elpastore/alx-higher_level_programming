#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:     # check if the list is not empty
        my_list.reverse()
        for rev in my_list:
            print("{:d}".format(rev))
