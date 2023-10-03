#!/usr/bin/python3

def print_last_digit(number):
    # Calculate the absolute value of the number to handle negative numbers.
    number = abs(number)
    # Extract the last digit by taking the remainder when dividing by 10.
    last_digit = number % 10
    print(last_digit, end="")
    return last_digit
