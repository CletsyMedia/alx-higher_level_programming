#!/usr/bin/python3
"""Module for creating Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
