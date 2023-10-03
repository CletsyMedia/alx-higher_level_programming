#!/usr/bin/python3
import random

# Generate a random number and assign it to the 'number' variable
number = random.randint(-10000, 10000)

# Calculate the last digit of the number
last_digit = abs(number) % 10

# Determine the message based on the last digit
if last_digit > 5:
    message = "greater than 5"
elif last_digit == 0:
    message = "0"
else:
    message = "less than 6 and not 0"

# Print the result with the required format
print(f"Last digit of {number} is {last_digit} and is {message}")
