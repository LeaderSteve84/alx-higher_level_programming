#!/usr/bin/python3
"""A module of a function that inserts a line of text
to a file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text
    to a file, after each line containing a specific string

    Args:
        filename (str): file name
        search_string (str): The string
        new_string (str): The string to insert
    """
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
