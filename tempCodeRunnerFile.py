#!/usr/bin/python3

# Start a loop to iterate from 0 to 9 for the first digit.
for a in range(10):
    # Start an inner loop to iterate from a + 1 to 9 for the second digit.
    for b in range(a + 1, 10):
        # Create the two-digit combination as a formatted string.
        combination = f"{a:02d}{b:02d}"
        # Print the combination followed by ", " if it's not the last combination.
        # Otherwise, print a new line.
        if a != 8 or b != 9:
            print(combination, end=", ")
        else:
            print(combination)
