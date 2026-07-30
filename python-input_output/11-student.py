#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Define a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the Student.

        If attrs is a list of strings, only the specified
        attributes are returned.
        """
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {
                attr: self.__dict__[attr]
                for attr in attrs
                if attr in self.__dict__
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance."""
        for key, value in json.items():
            setattr(self, key, value)
