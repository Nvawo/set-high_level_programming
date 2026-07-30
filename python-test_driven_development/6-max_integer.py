#!/usr/bin/python3
"""Module to find the max integer in a list."""


def max_integer(list=[]):
    """Return the biggest integer in a list.

    If the list is empty, return None.
    """
    if len(list) == 0:
        return None

    result = list[0]

    for item in list[1:]:
        if item > result:
            result = item

    return result
