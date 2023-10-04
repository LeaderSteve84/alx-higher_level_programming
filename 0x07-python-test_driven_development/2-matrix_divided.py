#!/usr/bin/python3
# 2-matrix_divided.py
'''a function that divides all elements of a matrix.'''


def matrix_divided(matrix, div):
    '''function that divides all elements of a matrix.

    Args:
        matrix (list): list of lists, int or floats.
        div (int or float): The divisor of the matrix.

    raises:
        TypeError: matrix must be a list of lists of integers or floats.
        TypeError: Each row of the matrix must be of the same size.
        TypeError: div must be a number (integer or float).
        ZeroDivisionError: div can’t be equal to 0
    Returns:
        Returns a new matrix.
    '''

    if (
        not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(
            isinstance(element, (int, float))
            for row in matrix for element in row
        )
    ):
        raise TypeError("matrix must be a matrix(list of lists) "
                        "of integers/floats")

    if not all(len(row) == len(matrix[0]) for now in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
