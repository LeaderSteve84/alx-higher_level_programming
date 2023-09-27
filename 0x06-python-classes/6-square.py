#!/usr/bin/python3
"""a class Square that defines a square by: (based on 5-square.py)"""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the class square.

        Args:
            size (int): The size of the square.
            position (int, int): The posittion of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the size attribute

        Args:
            value (int): The size to set.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the positon attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position attribute.

        Args:
            value (tuple): The position to set as a tuple
            of two positive integer.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square using the # character"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print("", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
