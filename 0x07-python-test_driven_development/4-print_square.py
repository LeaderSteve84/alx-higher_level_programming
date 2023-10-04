#!/usr/bin/python3
# 4-print_square.py
'''a function that prints a square with the character #.'''


def print_square(size):
    '''function that prints a square with the character #.

    Args:
        size (int): The size of the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
