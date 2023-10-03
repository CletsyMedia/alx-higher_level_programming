#!/usr/bin/python3

# Start a loop to iterate from 0 to 9 for the first digit.
for a in range(10):
    # Start an inner loop to iterate from a + 1 to 9 for the second digit.
    for b in range(a + 1, 10):
        # Print the combination of two digits separated by ", ".
        # Print a new line if it's the last combination.
        if a != 8 or b != 9:
            print("{:d}{:d}".format(a, b), end=", ")
        else:
            print("{:d}{:d}".format(a, b))
