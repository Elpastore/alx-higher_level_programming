#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) in range(97, 123):
            uppercase_char = chr(ord(letter) - ord('a') + ord('A'))
        else:
            uppercase_char = letter

        print(uppercase_char, end='')

    print()
