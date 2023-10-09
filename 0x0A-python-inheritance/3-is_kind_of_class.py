#!/usr/bin/python3
"""A module of a function that returns True if 
    the object is an instance of, or if the object
    is an instance of a class that inherited from,
    the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """function that checks.

    Args:
        obj (any): The object to be check
        a_class (type): a class that inherited from.

    Return:
        True if the object is an instance of, or if the object is an instance
        of a class that inherited from, the specified class ; otherwise False.
    """

    if isinstance(obj, a_class):
        return True
    return False
