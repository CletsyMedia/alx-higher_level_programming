#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Calculate the last digit
last_num = abs(number) % 10

# Define a function to determine the message based on the last digit
def get_msg(last_num):
    if last_num > 5:
        return "greater than 5"
    elif last_num == 0:
        return "0"
    else:
        return "less than 6 and not 0"

# Print the result
print(f"Last digit of {number} is {last_num} and is {get_msg(last_num)}\n")
