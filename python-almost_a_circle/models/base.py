#!/usr/bin/python3
"""Defines the Base class."""
import json


class Base:
    """Base class for all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of objects to a file."""
        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_objs = []

        list_dictionaries = [
            obj.to_dictionary() for obj in list_objs
        ]

        json_string = cls.to_json_string(list_dictionaries)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with attributes set from a dictionary."""
        raise NotImplementedError

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r", encoding="utf-8") as file:
                list_dicts = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []

        return [cls.create(**data) for data in list_dicts]
