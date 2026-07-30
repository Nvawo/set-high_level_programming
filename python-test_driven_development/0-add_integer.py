#!/usr/bin/python3
"""Module for adding two integers.

This module provides one function, ``add_integer``, that adds two
integers after validating their types. Float values are converted
to integers before the addition.
"""


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a: The first integer or float.
        b: The second integer or float. Defaults to 98.

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
