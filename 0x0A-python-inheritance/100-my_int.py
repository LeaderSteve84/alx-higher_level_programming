#!/usr/bin/python3
"""A module of a class MyInt that inherits from int:"""


class MyInt(int):
    """A class MyInt"""

    def __eq__(self, value):
        """overide == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Overide != operator with == behaviour."""
        return self.real == value
