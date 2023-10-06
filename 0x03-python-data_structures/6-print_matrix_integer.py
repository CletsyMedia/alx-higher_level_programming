#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Iterate through the rows and columns of the matrix
    for row in matrix:
        for i, num in enumerate(row):
            if i != len(row) - 1:
                print("{:d} ".format(num), end='') # Print integers with space
            else:
                print("{:d}".format(num)) # Print the last integer on the row
    if not matrix:
        print()  # Print an empty line if the matrix is empty
