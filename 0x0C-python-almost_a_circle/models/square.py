#!/usr/bin/python3
"""A module of a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a class of a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize the attributes of instance of class square.

        Args:
            size (int): The size
            x (int): The x attribute
            y (int): The y attribute
            id (int): The identity of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrieve the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the class Square..

        Args:
            *args (ints): various attribute values.
                - argument 1st - id attribute
                - argument 2nd - size attribute
                - argument 3th - x attribute
                - argument 4th - y attribute
            **kwargs (dict): key/value pair of attributes.
        """
        if args and len(args) != 0:
            n = 0
            for arg in args:
                if n == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif n == 1:
                    self.size = arg
                elif n == 2:
                    self.x = arg
                elif n == 3:
                    self.y = arg
                n += 1

        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    if j is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = j
                elif i == "size":
                    self.size = j
                elif i == "x":
                    self.x = j
                elif i == "y":
                    self.y = j

    def to_dictionary(self):
        """return the dict rep of a square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """return the print() and str() rep of the square"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))
