#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    len_argv = len(argv) - 1

    if len_argv == 0:
        print("0 arguments.")

    elif len_argv == 1:
        print("{:d} argument:".format(len_argv))
        print("{:d}: {}".format(1, argv[1]))

    else:
        print("{:d} arguments:".format(len_argv))
        for i in range(1, len_argv + 1):
            print("{:d}: {}".format(i, argv[i]))
