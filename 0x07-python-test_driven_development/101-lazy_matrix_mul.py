#!/usr/bin/python3
""" function that multiplies 2 matrices:."""
import numpy as n


def lazy_matrix_mul(m_a, m_b):
    """multiplication.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (n.matmul(m_a, m_b))
