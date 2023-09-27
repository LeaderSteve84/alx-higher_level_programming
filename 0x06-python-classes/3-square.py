#!/usr/bin/python3
"""class Square that define a Square"""


class Square:
    """a class Square that defines a square by: (based on 2-square.py)"""
    def __init__(self, size=0):
        """Initialize the class Square.

        Args:
            size (int): The size of the new Square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the area of the square"""
        return (self.__size * self.__size)
