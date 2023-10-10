#!/usr/bin/python3
"""A module of a class Square that inherits from
Rectangle (9-rectangle.py).
(task based on 10-square.py).
"""


class Square(Rectangle):
    """A class Square"""

    def __init__(self, size):
        """Initialize the attributes of the object.

        Args:
            size (int): The size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
