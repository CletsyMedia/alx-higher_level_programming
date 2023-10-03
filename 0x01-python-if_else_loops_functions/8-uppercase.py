#!/usr/bin/python3

def uppercase(s):
    """
    Prints the input string in uppercase followed by a new line.

    :param s: The input string.
    """
    result = ""  # Initialize an empty string to store the result.

    # Iterate through the characters in the input string.
    for char in s:
        # Check if the character is a lowercase letter.
        if 'a' <= char <= 'z':
            # Convert it to uppercase using ASCII values.
            result += chr(ord(char) - ord('a') + ord('A'))
        else:
            # Keep the character unchanged if it's not a lowercase letter.
            result += char

    # Print the result followed by a new line.
    print(result, end="\n")
