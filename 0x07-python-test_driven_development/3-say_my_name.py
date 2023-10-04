#!/usr/bin/python3
# 3-say_my_name.py
'''a function that prints My name is <first name> <last name>'''


def say_my_name(first_name, last_name=""):
    ''' function that prints My name is <first name> <last name>.

    Args:
        first_name (string): The first name
        last_name (string): The last name

    Raises:
        TypeError: first_name and last_name must be strings
    '''

    if not ininstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
