#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
if digit > 5:
    show = "and is greater than 5"
elif digit == 0:
    show = "and is 0"
else:
    show = "and is less than 6 and not 0"
print("Last digit of", number, "is", digit, show)
