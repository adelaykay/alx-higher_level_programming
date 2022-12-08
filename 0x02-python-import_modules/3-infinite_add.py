#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    n = len(argv) - 1
    sum = 0

    while n >= 1:
        sum += int(argv[n])
        n -= 1
    print("{}".format(sum))
