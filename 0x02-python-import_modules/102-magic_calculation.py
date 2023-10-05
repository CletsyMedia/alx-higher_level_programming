def magic_calculation(a, b):
    # Initialize add and sub to None
    add, sub = None, None

    # Check if a is less than b
    if a < b:
        # Import the 'add' and 'sub' functions from 'magic_calculation_102'
        add = __import__('magic_calculation_102').add
        sub = __import__('magic_calculation_102').sub

        # Perform the 'add' operation with a and b
        c = add(a, b)

        # Loop from 4 to 5 (inclusive) and add each value to 'c'
        for i in range(4, 6):
            c = add(c, i)

        # Return the final result
        return c

    # If a != less than b, perform the 'sub' operation and return the result
    return sub(a, b)
