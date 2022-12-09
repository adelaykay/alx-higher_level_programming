#!/usr/bin/python3


def max_integer(my_list=[]):
    if not (len(my_list)):
        return
    else:
        max_int = my_list[0]
        n = 1
        while n < len(my_list):
            if max_int < my_list[n]:
                max_int = my_list[n]
            n += 1
        return(max_int)
