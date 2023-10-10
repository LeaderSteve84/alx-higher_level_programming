#!/usr/bin/python3
"""A module of a function that adds a new
attribute to an object if it’s possible:
"""


def add_attribute(obj, attri, value):
    """A method to add a new attribute.

    Args:
        obj (any): The object
        attri (str): The name of attribute
        value (any): The value

    Raises:
        TypeError: If the attribute cannot be added.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attri, value)
