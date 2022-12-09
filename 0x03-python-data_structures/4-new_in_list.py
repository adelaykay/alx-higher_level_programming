#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    n = list(my_list)
    if len(my_list) < idx or idx < 0:
        return(n)
    else:
        n[idx] = element
        return(n)
