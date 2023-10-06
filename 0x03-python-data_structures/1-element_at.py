#!/usr/bin/python3
def element_at(my_list, idx):

    numb = list(range(0, len(my_list)))
    # if (idx > 0 and idx <= len(my_list)):

    if (idx >= 0 and idx in numb):
        return my_list[idx]
    else:
        return None
