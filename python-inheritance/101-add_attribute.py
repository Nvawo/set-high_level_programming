#!/usr/bin/python3
"""Module that defines add_attribute."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if possible.

    Raises:
        TypeError: If the object does not allow new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
