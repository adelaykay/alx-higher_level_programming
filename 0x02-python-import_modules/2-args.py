#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    n = len(argv) - 1
    if n == 0:
        print("{} arguments.".format(n))
    elif n == 1:
        print("{} argument:".format(n))
        print("{}: {}".format(n, argv[n]))
    elif n > 1:
        print("{} arguments:".format(n))
        i = 1
        while n:
            print("{}: {}".format(i, argv[i]))
            n -= 1
            i += 1
