#!/usr/bin/python3
def magic_calculation(a, b):
    # Import 'add' and 'sub' functions from 'magic_calculation_102' module.
    from magic_calculation_102 import add, sub

    # Check if 'a' is less than 'b'.
    if a < b:
        # Initialize 'c' to the result of adding 'a' and 'b'.
        c = add(a, b)

        # Iterate over a range from 4 to 6 (inclusive).
        for i in range(4, 7):
            # Add 'i' to 'c' and store the result in 'c'.
            c = add(c, i)

        # Return the final result 'c'.
        return c
    else:
        # If 'a' is greater than or equal to 'b', subtract 'b' from 'a' and return the result.
        return sub(a, b)
