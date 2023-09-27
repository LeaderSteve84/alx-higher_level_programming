#!/usr/bin/python3
"""a class Square that defines a square by: (based on 4-square.py)"""


class Square:
    def __init__(self, size=0):
        """Initalize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrive the size attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size attribute.
        Args:
        value (int): The size to set.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square using # character"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
