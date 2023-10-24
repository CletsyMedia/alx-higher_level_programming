#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square with the given size.

        Args:
            size (int or float): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int or float): The new size for the square.

        Raises:
            TypeError: If the value is not a number.
            ValueError: If the value is less than 0.
        """
        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares have equal area.

        Args:
            other (Square): The square to compare with.

        Returns:
            True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares have different area.

        Args:
            other (Square): The square to compare with.

        Returns:
            True if the areas are different, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if the area of this square is less than the other square.

        Args:
            other (Square): The square to compare with.

        Returns:
            True if this square's area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the area of this square is less than or equal to the other square.

        Args:
            other (Square): The square to compare with.

        Returns:
            True if this square's area is less or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if the area of this square is greater than the other square.

        Args:
            other (Square): The square to compare with.

        Returns:
            True if this square's area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the area of this square is greater than or equal to the other square.

        Args:
            other (Square): The square to compare with.

        Returns:
            True if this square's area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()


if __name__ == "__main":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
