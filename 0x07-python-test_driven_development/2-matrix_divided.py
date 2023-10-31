#!/usr/bin/python3
"""
2-matrix_divided module
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.

    Args:
        - matrix (list of lists): matrix containing integers or floats.
        - div (int or float): The divisor for division.

    Raises:
        - TypeError: Checks for the type of the matrix
                    (list of lists) and the types of its elements.
        - ZeroDivisionError: Checks for invalid division when div is 0.

    Returns:
        - A new matrix with elements rounded to 2 decimal places.
    """

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix
                        (list of lists) of integers/floats")

    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError("matrix must be a matrix
                        (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(i / div, 2) for i in row] for row in matrix]

    return result
