#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Define the __init__ function."""

    def __init__(self, size=0):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
