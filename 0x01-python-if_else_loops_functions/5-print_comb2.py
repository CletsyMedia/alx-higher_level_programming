#!/usr/bin/python3
# Start a loop to iterate from 0 to 99 (inclusive).
for a in range(100):
    # Check if the current number is less than 10 (single-digit number).
    if a < 10:
        # If the number is less than 10, print it with a leading zero.
        # Use end=", " if it's not the last number; otherwise,
        # use end="\n" to start a new line.
        print("0{}".format(a), end=", " if a != 99 else "\n")
    else:
        # If the number is 10 or greater, print it without a leading zero.
        # Use end=", " if it's not the last number; otherwise, 
        # use end="\n" to start a new line.
        print(a, end=", " if a != 99 else "\n")
