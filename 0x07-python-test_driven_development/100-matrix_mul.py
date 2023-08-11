#!/usr/bin/python3
"""functio"""


def matrix_mul(m_a, m_b):
    """matrix_mul hat multiplies two matrix
    Args:
        m_a : first matrix
        m_b : second matrix
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    col = 0
    row = 0

    if m_a == []:
        raise ValueError("m_a can't be empty")
    for r in m_a:
        if type(r) != list:
            raise TypeError("m_a must be a list of lists")
        len1 = len(m_a[0])
        if r == []:
            raise ValueError("m_a can't be empty")
        if len1 != len(r):
            raise TypeError("each row of m_a must be of the same size")
        col = len(r)
        for c in r:
            if type(c) != int and type(c) != float:
                raise TypeError("m_a should contain only integers or floats")

    if m_b == []:
        raise ValueError("m_b can't be empty")
    for ro in m_b:
        if type(ro) != list:
            raise TypeError("m_b must be a list of lists")
        len2 = len(m_b[0])
        if ro == []:
            raise ValueError("m_b can't be empty")
        if len2 != len(ro):
            raise TypeError("each row of m_b must be of the same size")
        row += 1
        for co in ro:
            if type(co) != int and type(co) != float:
                raise TypeError("m_b should contain only integers or floats")

    if col != row:
        raise ValueError("m_a and m_b can't be multiplied")

    matrix_1 = []

    for row1 in m_a:
        l1 = 0
        l_row1 = []
        while l1 < len(m_b[0]):
            res = 0
            k = 0
            for c1 in row1:
                res += c1 * m_b[k][l1]
                k += 1
            l_row1.append(res)
            l1 += 1
        matrix_1.append(l_row1)

    return matrix_1
