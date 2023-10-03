#!/usr/bin/python3
def remove_char_at(str, n):
    if (len(str) >= n and n >= 0):
        copy_str = str[0:n] + str[n+1:]
        return copy_str
    else:
        return str
