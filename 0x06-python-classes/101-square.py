#!/usr/bin/python3
"""Define a class Square that defines a square."""


class Square:
    """Represent a square.

    Attributes:
        __size (int): size of a side of the square
        __position (tuple): position of the square in 2D space
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square.

        Args:
            size (int): The size of a side of the square.
            position (tuple): The position of the square in 2D space.
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculate the square's area.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            The size of the square.
        """
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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square in 2D space.

        Returns:
            The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square in 2D space.

        Args:
            value (tuple): The new position for the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or value[0] < 0 or
                not isinstance(value[1], int) or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square with '#' characters using position for spacing.

        The position is used to insert spaces before printing the '#' characters.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            A string that represents the square as specified.
        """
        square_str = ""
        if self.__size == 0:
            square_str += "\n"
        else:
            for _ in range(self.__position[1]):
                square_str += "\n"
            for _ in range(self.__size):
                square_str += " " * \
                    self.__position[0] + "#" * self.__size + "\n"
        return square_str.strip()


if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
