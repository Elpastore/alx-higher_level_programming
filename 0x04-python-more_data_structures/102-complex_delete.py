#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    new = a_dictionary.copy()
    for key, values in new.items():
        if values == value:
            del a_dictionary[key]
    return a_dictionary
