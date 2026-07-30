#!/usr/bin/python3
"""Module that creates a Python object from a JSON file."""

import json


def load_from_json_file(filename):
    """Return the Python object represented by a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
