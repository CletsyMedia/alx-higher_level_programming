#!/usr/bin/python3

"""
This module defines a class Rectangle.

It is based on the 5-rectangle.py module.
"""



class Rectangle:
    """A class that defines a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle (default is 0).
            height (int, optional): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.

        Returns:
            str: A string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""

        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """
        Return a string representation of the rectangle for eval().

        Returns:
            str: A formal string representation of the rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Print a message when an instance of Rectangle is deleted.
        Decrements the number_of_instances class attribute.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
