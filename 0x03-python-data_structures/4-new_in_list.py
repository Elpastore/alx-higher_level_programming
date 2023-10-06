#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    numb = list(range(len(my_list)))

    if (idx >= 0 and idx in numb):
        new_list = []

        for i in range(0, (len(my_list))):
            new_list.append(my_list[i])

        new_list[idx] = element
        return new_list
    else:
        return my_list
