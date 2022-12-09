#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if my_list:
        isEven = []
        for num in my_list:
            isEven.append(num % 2 == 0)
        return(isEven)
