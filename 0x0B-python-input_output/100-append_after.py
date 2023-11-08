#!/usr/bin/python3
"""
100-append_after module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    insert a line of the text after specific string
    """
    with open(filename, "r", encoding="utf-8") as file:
        line_list = file.readlines()    # store each line to the line_list

    with open(filename, "w", encoding="utf-8") as file:
        for line in line_list:
            file.write(line)

            if search_string in line:
                file.write(new_string)
