#!/usr/bin/python3
"""Defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width."""
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height."""
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate."""
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate."""
        self.__y = value
