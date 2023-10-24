#!/usr/bin/python3
class Square:
    """Define a class Square."""

    def __init__(self, size=0):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        self.__size = size

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2


