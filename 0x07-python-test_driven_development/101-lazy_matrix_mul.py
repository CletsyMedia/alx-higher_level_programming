#!/usr/bin/env python3
"""
Defines lazy_matrix function
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy

    Args:
        m_a (list of lists): First matrix
        m_b (list of lists): Second matrix

    Returns:
        numpy.ndarray: Result of the matrix multiplication
    """
    return np.dot(m_a, m_b)
