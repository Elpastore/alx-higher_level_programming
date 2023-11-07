#!/usr/bin/python3
"""
script that add argument then save it
"""

import os
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


my_list = []
argument = sys.argv

if not os.path.exists("./add_item.json"):
    save_to_json_file(my_list, "add_item.json")

my_list = load_from_json_file("add_item.json")

for i in argument[1:]:
    my_list.append(i)
save_to_json_file(my_list, "add_item.json")
