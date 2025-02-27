#!/usr/bin/python3
import random

number = random.randint(-10, 10)


def random_number(int):

    if int > 0:
        print(f"{int} is positive")
    elif int < 0:
        print(f"{int} is negative")
    else:
        print(f"{int} is zero")
random_number(number)
