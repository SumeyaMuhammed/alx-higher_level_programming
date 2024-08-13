#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
if number < 0:
    lastDigit = -10 + lastDigit
elif lastDigit == 0:
    lastDigit = 0
if lastDigit > 5:
    desc = "and is greater than 5"
elif lastDigit == 0:
    desc = "and is 0"
elif 0 < lastDigit < 6:
    desc = "and is less than 6 and not 0"
print(f"Last digit of {number} is {lastDigit} {desc}")
