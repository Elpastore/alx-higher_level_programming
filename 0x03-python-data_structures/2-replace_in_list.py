#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    numb = list(range(len(my_list)))
    if (idx >= 0 and idx in numb):
        my_list[idx] = element
    return my_list
