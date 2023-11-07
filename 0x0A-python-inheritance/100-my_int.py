#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Class representing an integer with inverted equality operators.

    Args:
        value (int): The integer value to be stored.

    Attributes:
        value (int): The integer value stored within the object.
    """

    def __init__(self, value):
        super().__init__(value)

    def __eq__(self, other):
        """Override the equality operator (==) with inequality behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator (!=) with equality behavior."""
        return super().__eq__(other)
