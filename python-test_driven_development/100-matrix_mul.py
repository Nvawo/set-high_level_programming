#!/usr/bin/python3
"""Module for matrix multiplication."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a: First matrix.
        m_b: Second matrix.

    Returns:
        A new matrix containing the product.

    Raises:
        TypeError: If matrices are invalid.
        ValueError: If matrices are empty or incompatible.
    """

    # m_a validation
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if not all(
        all(isinstance(x, (int, float)) for x in row)
        for row in m_a
    ):
        raise TypeError("m_a should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    # m_b validation
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(
        all(isinstance(x, (int, float)) for x in row)
        for row in m_b
    ):
        raise TypeError("m_b should contain only integers or floats")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []

    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
            row.append(total)
        result.append(row)

    return result
