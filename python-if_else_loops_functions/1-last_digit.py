#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
def random_signed_number(int):
    if int >= 0:
        x = int % 10
        if x > 5:
            print(f"Last digit of {int} is {x} and is greater than 5")
        elif x == 0:
            print(f"Last digit of {int} is {x} and is 0")
        elif x < 6 & x != 0:
            print(f"Last digit of {int} is {x} and is less than 6 and not 0")
    else:
        x = -int % 10
        y = -x
        print(f"Last digit of {int} is {y} and is less than 6 and not 0")

random_signed_number(number)
