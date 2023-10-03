#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Find the last number
last_num = abs(number) % 10
# Determine the appropriate message
if last_num > 5:
    msg = "and is greater than 5"
elif last_num == 0:
    msg = "and is 0"
else:
    msg = "and is less than 6 and not 0"
# Printing the result
print(f"Last digit of {number} is {last_num} {msg}")
