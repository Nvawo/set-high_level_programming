#!/usr/bin/python3
"""Module that defines the matrix_divided function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with all elements divided by div.

    Raises:
        TypeError: If matrix is invalid or div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])

    for row in matrix:
        if len(row) != row_length:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )

        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(item / div, 2) for item in row]
        for row in matrix
    ]
