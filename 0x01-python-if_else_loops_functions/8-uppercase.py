#!/usr/bin/python3
def islower(c):
    """Return True if c is lowercase, false if not"""
    return(122 >= ord(c) >= 97)


def uppercase(str):
    """Prints a string in uppercase followed by a new line"""
    for char in str:
        if islower(char):
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print("{}".format(char), end="")
    print("")
