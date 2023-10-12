#!/usr/bin/python3
"""A module of a class BaseGeometry
(based on 6-base_geometry.py).
"""


class BaseGeometry:
    """a class of BaseGeometry"""

    def area(self):
        """a method area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value.

        Args:
            name (string): A string.
            value (int): an integer value.

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
