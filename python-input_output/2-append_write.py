#!/usr/bin/python3
"""Module that appends a string to a UTF-8 text file."""


def append_write(filename="", text=""):
    """Append a string to a text file.

    Return the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
