#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if isinstance(number, int):
    if number > 0:
        print(f"{number} is positive")
    elif number == 0:
        print(f"{number} is zero")
    else:
        print(f"{number} is negative")
else:
    print("wrong type")
    
