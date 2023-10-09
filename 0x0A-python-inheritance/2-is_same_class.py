#!/usr/bin/python3
"""A module of a function that returns True if the object is exactly
    an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """function that returns True if the object is exactly
    an instance of the specified class ; otherwise False.

    Args:
        obj (any): The object/instance to be check
        a_class (class): The class to match the type of class

    Return:
        True if the object is exactly an instance of the
        specified class ; otherwise False.

    """
    if type(obj) == a_class:
        return True
    else:
        return False
