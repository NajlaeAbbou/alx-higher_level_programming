#!/usr/bin/python3
"""Pascal's Triangle function."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the triangle."""
    if n <= 0:
        return []

    tr = [[1]]
    while len(tr) != n:
        ti = tr[-1]
        tp = [1]
        for i in range(len(ti) - 1):
            tp.append(ti[i] + ti[i + 1])
        tp.append(1)
        tr.append(tp)
    return tr
