#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers in the specified format.

    Args:
        matrix (list of lists): The matrix of integers to be printed.

    Format:
        Each row is printed on a separate line, with integers separated by spaces.

    Example:
        For matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
        Output:
            1 2 3
            4 5 6
            7 8 9

    If the matrix is empty, an empty line is printed.
    """
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))
