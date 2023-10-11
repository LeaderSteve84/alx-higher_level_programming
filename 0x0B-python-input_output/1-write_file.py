#!/usr/bin/python3
"""A module of a function that writes a string to a text
file (UTF8) and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (string): The name of the file to write.
        text (int): The text

    Return:
        The number of characters written:number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
