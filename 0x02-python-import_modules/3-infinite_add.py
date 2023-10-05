#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    argv = sys.argv
    len_argv = len(argv) - 1
    sum_argv = 0

    if len_argv == 0:
        print("{:d}".format(sum_argv))

    else:
        for i in range(1, len_argv + 1):
            sum_argv += int(argv[i])
        print("{:d}".format(sum_argv))
