#!/usr/bin/python3

"""A module of a model class bass"""

# import json
# import csv
# import turtle


class Base:
    """Base class

    Private class attribute:
        __nb_objects (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the attributes of the instance.

        Args:
            id (int): The identity
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
