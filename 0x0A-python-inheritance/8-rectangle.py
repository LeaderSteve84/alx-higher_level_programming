#!/usr/bin/python3
"""A module of a class Rectangle that inherits
from BaseGeometry (7-base_geometry.py).
"""


class Rectangle(BaseGeometry):
    """A class of a Rectangle"""

    def __init__(self, width, height):
        """Initialize the attribute of the new
        Rectangle.

        Args:
            width (int): The width
            height (int): The height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
