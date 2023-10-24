#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Define the __init__ function."""

    def __init__(self, size=0):
        """Initialize the size of the square.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        """if statement"""
        if type(value) is not int:
            """raise error"""
            raise TypeError("size must be an integer")
        elif value < 0:
            """raise error"""
            raise ValueError("size must be >= 0")
        else:
            """initialize"""
            self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

