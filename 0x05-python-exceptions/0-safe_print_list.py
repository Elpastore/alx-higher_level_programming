#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    if my_list:
        try:
            count = 0
            for numb in range(0, x):
                print("{}".format(my_list[numb]), end="")
                count += 1
        except IndexError:
            pass
        print()
        return count
