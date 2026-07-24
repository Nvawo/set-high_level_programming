#!/usr/bin/python3
"""Module defines a locked class."""


class LockedClass:
    """Class that only allows the first_name attribute."""
    __slots__ = ["first_name"]
