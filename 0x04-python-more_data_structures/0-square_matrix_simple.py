#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for i in matrix:
        square = list(map(lambda x: x**2, i))
        result = result + square
    return result
