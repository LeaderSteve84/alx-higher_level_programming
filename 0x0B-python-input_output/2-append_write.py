#!/usr/bin/python3
"""function that appends a string at the end of a text
file (UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text
    file (UTF8) and returns the number of characters added:
    
    Args:
        filename (string): The file name
        text (string): The string to append to the file.

    Return:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
