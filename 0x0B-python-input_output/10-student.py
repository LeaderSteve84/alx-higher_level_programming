#!/usr/bin/python3
"""A module of a  class Student that defines a student by:"""


class Student:
    """A class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize the attribtes of the object of the class

        Args:
            first_name (str): The first name
            last_name (str): The last name
            age (int): The age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation
        of a Student instance

        if attrs is a list of strings, represents only those
        attributes that are in the list.

        Args:
            attrs (list): (optional) The attribute to represent.
        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
