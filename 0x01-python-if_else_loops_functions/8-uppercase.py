#!/usr/bin/python3
def uppercase(str):
    # Initialize an empty result string.
    result = ""

    # Iterate through the characters in the input string.
    for c in str:
        # Check if the character is a lowercase letter.
        if 'a' <= c <= 'z':
            # Convert it to uppercase and append it to the result string.
            result += chr(ord(c) - ord('a') + ord('A'))
        else:
            # If it's not a lowercase letter, keep it unchanged.
            result += c

    # Print the result string followed by a new line.
    print(result)


# Test cases
uppercase("best")
uppercase("Best School 98 Battery street")
