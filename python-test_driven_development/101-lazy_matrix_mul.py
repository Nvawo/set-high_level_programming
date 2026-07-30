#!/usr/bin/python3
"""Module that multiplies two matrices using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy.

    Args:
        m_a: First matrix.
        m_b: Second matrix.

    Returns:
        The product of the two matrices.

    Raises:
        ValueError: If the matrices cannot be multiplied.
    """
    return np.matmul(m_a, m_b)
