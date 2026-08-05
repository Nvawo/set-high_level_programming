#!/usr/bin/python3
"""Defines the Base class."""

import json
import csv


class Base:
    """Base class for all other classes in the project."""

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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of objects to a file."""
        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_objs = []

        list_dictionaries = []
        for obj in list_objs:
            list_dictionaries.append(obj.to_dictionary())

        json_string = cls.to_json_string(list_dictionaries)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r", encoding="utf-8") as file:
                json_string = file.read()
        except FileNotFoundError:
            return []

        list_dictionaries = cls.from_json_string(json_string)

        return [cls.create(**dictionary)
                for dictionary in list_dictionaries]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize objects to CSV."""
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if list_objs is None:
                return

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([
                        obj.id,
                        obj.width,
                        obj.height,
                        obj.x,
                        obj.y
                    ])
                elif cls.__name__ == "Square":
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
        instances = []

        try:
            with open(filename, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)

                for row in reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                        }
                    elif cls.__name__ == "Square":
                        dictionary = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                        }
                    else:
                        continue

                    instances.append(cls.create(**dictionary))

        except FileNotFoundError:
            return []

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw all Rectangles and Squares."""
        import turtle

        screen = turtle.Screen()
        screen.title("Almost a Circle")
        screen.bgcolor("white")

        pen = turtle.Turtle()
        pen.speed(0)
        pen.pensize(2)

        def draw_shape(x, y, width, height, color):
            """Draw one rectangle or square."""
            pen.penup()
            pen.goto(x, y)
            pen.setheading(0)
            pen.pendown()

            pen.pencolor(color)
            pen.fillcolor(color)
            pen.begin_fill()

            pen.forward(width)
            pen.right(90)
            pen.forward(height)
            pen.right(90)
            pen.forward(width)
            pen.right(90)
            pen.forward(height)
            pen.right(90)

            pen.end_fill()

        for rectangle in list_rectangles:
            draw_shape(
                rectangle.x,
                -rectangle.y,
                rectangle.width,
                rectangle.height,
                "blue"
            )

        for square in list_squares:
            draw_shape(
                square.x,
                -square.y,
                square.size,
                square.size,
                "red"
            )

        pen.hideturtle()
        screen.mainloop()
