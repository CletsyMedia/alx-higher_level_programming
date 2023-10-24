#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """
    This is the Square class.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance with optional size.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square. (default is 0)

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
       """ if statement """
        if type(size) != int:
            """ raise an error """
            raise TypeError("size must be an integer")
        elif size < 0:
            """ raise an error """
            raise ValueError("size must be >= 0")
        else:
            """ initialize __size of self with size """
            self.__size = size
            