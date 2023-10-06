#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for check in my_list:
        new_list.append(True if check % 2 == 0 else False)
    return new_list
