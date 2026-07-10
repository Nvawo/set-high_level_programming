#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list."""
    unique = set(my_list)
    total = 0

    for number in unique:
        total += number

    return total
