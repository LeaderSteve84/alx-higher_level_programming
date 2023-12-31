#!/usr/bin/python3
"""a module of a class MyList that inherits from list"""


class MyList(list):
    """ a class MyList that inherits from list
    """
    def __init__(self, input_list=None):
        if input_list is None:
            super().__init__()
        elif isinstance(input_list, list):
            super().__init__(input_list)
        else:
            super().__init__([input_list])

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
