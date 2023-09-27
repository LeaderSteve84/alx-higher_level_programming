#!/usr/bin/python3
"""a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """a class Square that defines a square by: (based on 3-square.py)"""
    def __init__(self, size=0):
        """Initialize the class Square.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrive the size attribute, """
        return self.__size

    @size.setter
    def size(self, value):
        """set the size attribute.

        Args:
            value (int): The size to set.
         """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square"""
        return (self.__size * self.__size)
