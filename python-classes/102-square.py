#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize a square."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equal to."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal to."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to."""
        return self.area() >= other.area()
