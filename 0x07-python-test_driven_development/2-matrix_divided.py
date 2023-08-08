#!/usr/bin/python3
""" function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """divides matrix by scalar integerwith two decimal places"""
    import decimal
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    rows = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        rows.append(len(row))
        for el in row:
            if type(el) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(rows)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    matrix_1 = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))
    return matrix_1
