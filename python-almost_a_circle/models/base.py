#!/usr/bin/python3
"""Defines the Base class."""
import json
import csv


class Base:
    """Base class for the project."""

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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of objects to a file."""
        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_objs = []

        list_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize objects to CSV."""
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if list_objs is None:
                return

            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([
                        obj.id,
                        obj.width,
                        obj.height,
                        obj.x,
                        obj.y
                    ])

            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([
                        obj.id,
                        obj.size,
                        obj.x,
                        obj.y
                    ])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize objects from CSV."""
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)

                if cls.__name__ == "Rectangle":
                    for row in reader:
                        if row:
                            dictionary = {
                                "id": int(row[0]),
                                "width": int(row[1]),
                                "height": int(row[2]),
                                "x": int(row[3]),
                                "y": int(row[4])
                            }
                            yield_instance = cls.create(**dictionary)
                            if yield_instance is not None:
                                yield_instance

                elif cls.__name__ == "Square":
                    for row in reader:
                        if row:
                            dictionary = {
                                "id": int(row[0]),
                                "size": int(row[1]),
                                "x": int(row[2]),
                                "y": int(row[3])
                            }
                            yield_instance = cls.create(**dictionary)
                            if yield_instance is not None:
                                yield_instance

        except FileNotFoundError:
            return []

        return []
