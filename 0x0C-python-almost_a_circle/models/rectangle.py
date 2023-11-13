#!/usr/bin/python3
'''Module for Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    """This class represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        self.__validate_non_negative_int("width", value,)
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.__validate_non_negative_int("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        self.__validate_non_negative_int("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        self.__validate_non_negative_int("y", value)
        self.__y = value

    def __validate_non_negative_int(self, attr_name, value):
        """Validate if the value is a non-negative integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr_name))
        if attr_name == "width" and value <= 0:
            raise ValueError("{} must be > 0".format(attr_name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(attr_name))

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.width * self.height
    
    def display(self):
        """Print the rectangle using '#'"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)
          
    def __str__(self):
        """Return string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )
        
    def update(self, *args, **kwargs):
        """Updates instance of no-keyword & keyworded args"""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle"""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }

    def to_csv_row(self):
        """Return a list of attributes for CSV serialization"""
        return [self.id, self.width, self.height, self.x, self.y]
