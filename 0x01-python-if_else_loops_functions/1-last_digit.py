#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of "
ld = number % 10
if number < 0:
    ld = -((number * -1)%10)
if ld > 5:
    print(f"{str1}{number} is {ld} and is greater than 5")
elif ld == 0:
    print(f"{str1}{number} is {ld} and is 0")
elif 6 > ld != 0:
    print(f"{str1}{number} is {ld} and is less than 6 and not 0")
