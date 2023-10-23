#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for numb in range(x):
        try:
            print("{}".format(my_list[numb]), end="")
            count += 1
        except IndexError:
            pass
    print("")
    return count
