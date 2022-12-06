#!/usr/bin/python3
def islower(c):
    """Return True if c is lowercase, false if not"""
    return(122 >= ord(c) >= 97)


def uppercase(str):
    """Prints a string in uppercase followed by a new line"""
    new_str = ""
    for char in str:
        if islower(char):
            new_str += f"{chr(ord(char) - 32)}"
        else:
            new_str += f"{char}"
    print("{}".format(new_str))
