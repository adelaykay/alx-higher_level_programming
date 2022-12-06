#!/usr/bin/python3
def print_last_digit(number):
    """Returns the value of the last digit"""
    if number < 0:
        last_digit = (number * -1) % 10
    else:
        last_digit = number % 10
    print(f"{last_digit}", end="")
    return(last_digit)
