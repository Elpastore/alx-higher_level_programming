#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) in range(97, 123):
            uppercase_letter = chr(ord(letter) - ord('a') + ord('A'))
        else:
            uppercase_letter = letter

        print("{}".format(uppercase_letter), end='')

    print()
