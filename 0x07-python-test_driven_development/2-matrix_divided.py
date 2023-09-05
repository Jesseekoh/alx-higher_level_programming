#!/usr/bin/python3
"""
2-matrix_divided
This module supplies one function, matrix_divided().
"""


def matrix_divided(matrix, div):
    """Divides all he elements of a matrix by a specified number

    Args:
        matrix (list): matrix
        div (int, float): divider
    """

    row_len = 0
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if len(row) is not row_len and row_len != 0:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
