def magic_calculation(a, b):
    # Initialize 'add' and 'sub' variables to None.
    add = None
    sub = None

    # Check if 'a' is less than 'b'.
    if a < b:
        # Import 'add' and 'sub' functions from 'magic_calculation_102'.
        from magic_calculation_102 import add, sub

        # Call 'add' function with arguments 'a' and 'b'.
        return add(a, b)
    else:
        # If 'a' is greater than or equal to 'b', call 'sub'
        # function with arguments 'a' and 'b'.
        return sub(a, b)
