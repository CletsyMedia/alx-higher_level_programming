#!/usr/bin/python3
import random

# Keep the random number generation line unchanged
number = random.randint(-10000, 10000)

# Calculate the last digit of the number
last_digit = abs(number) % 10

# Determine the appropriate message
if last_digit > 5:
    message = "and is greater than 5"
elif last_digit == 0:
    message = "and is 0"
else:
    message = "and is less than 6 and not 0"

# Print the result
if number < 0:
    last_digit = -last_digit
print(f"Last digit of {number:d} is {last_digit:d} {message}")
