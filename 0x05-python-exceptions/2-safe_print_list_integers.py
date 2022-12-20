#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0
    try:
        while i < x:
            if type(my_list[i]) == type(3):
                print("{:d}".format(my_list[i]), end="")
                count += 1
            i += 1
        print()
        return (count)
    except IndexError:
        raise
