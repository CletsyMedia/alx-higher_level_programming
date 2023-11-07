#!/usr/bin/python3
"""Module that defines an empty class BaseGeometry.
"""


class BaseGeometry:
    """Geometry Class
    """
    
    def area(self):
        """Calculate the area of the shape.
            Returns:
                float: area
          Raises:
            Exception: Always raises an Exception with the message
                       "area() is not implemented."
        """
        raise Exception("area() is not implemented")
