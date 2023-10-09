#!/usr/bin/python3
'''a script of a function that returns the list of
available attributes and methods of an object.
'''


def lookup(obj):
    '''function that returns the list of available
    attributes and methods of an object

    Args:
        obj (class): class inherited

    Return: List of attributes and methods
    '''
    return(dir(obj))
