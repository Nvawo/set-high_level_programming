#!/usr/bin/python3
"""Module that inserts a line of text after a given string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after each line containing search_string."""
    updated_text = ""

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            updated_text += line
            if search_string in line:
                updated_text += new_string

    with open(filename, "w", encoding="utf-8") as file:
        file.write(updated_text)
