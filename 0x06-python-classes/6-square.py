#!/usr/bin/python3
class Square:
    """Define a class Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): The position of the square. Default is (0, 0).

        Raises:
            TypeError: If the size is not an integer or if the position is not a tuple of 2 positive integers.
            ValueError: If the size is less than 0.
        """
        self.size = size
        self.position = position

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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position for the square.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if (
            type(value) is not tuple
            or len(value) != 2
            or type(value[0]) is not int
            or type(value[1]) is not int
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#' and use position for spacing."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)


if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_1.my_print()
    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()
    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()
    print("--")
