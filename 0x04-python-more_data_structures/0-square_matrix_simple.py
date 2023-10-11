#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_matrix = []
    for row in matrix:
        square_row = []     # create list to store row items

        for colon in row:
            square_row.append(colon**2)
        new_matrix.append(square_row)
    return new_matrix
