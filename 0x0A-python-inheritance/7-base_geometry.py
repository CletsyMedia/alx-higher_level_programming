#!/usr/bin/python3

"""Module that defines a class BaseGeometry.
"""

class BaseGeometry:
    """Class that defines a shape.
    """
    def area(self):
        """
        Calculate the area of the shape.

        Raises:
            Exception: Always raises an Exception with the message
                       "area() is not implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Args:
            name (str): A string representing the name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
