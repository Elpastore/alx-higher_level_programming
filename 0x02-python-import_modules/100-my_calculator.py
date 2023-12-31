#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    argv = sys.argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        signe = str(argv[2])

        if signe == '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif signe == '-':
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif signe == '*':
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif signe == '/':
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
