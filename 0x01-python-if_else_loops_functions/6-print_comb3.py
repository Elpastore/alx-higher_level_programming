#!/usr/bin/python3
for a in range(0, 8):
    for b in range(a + 1, 10):
        print("{}{}, ".format(a, b), end="")
print("{}{}".format(a + 1, b))
