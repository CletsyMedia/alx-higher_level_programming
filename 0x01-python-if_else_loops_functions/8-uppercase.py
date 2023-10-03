#!/usr/bin/python3

def uppercase(str):
    """
    Prints the input string in uppercase followed by a new line.

    :param str: The input string.
    """
    for char in str:
        # Check if the character is a lowercase letter.
        if 'a' <= char <= 'z':
            # Convert it to uppercase using ASCII values.
            char = chr(ord(char) - ord('a') + ord('A'))
        print(char, end="")  # Print each character without a newline
    print('')  # Print a newline after processing the entire string
