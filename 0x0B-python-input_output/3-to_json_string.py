#!/usr/bin/python3
"""A module of a function that returns the JSON
representation of an object (string):
"""


def to_json_string(my_obj):
    """function that returns the JSON
    representation of an object (string)
    """
    return json.dumps(my_obj)