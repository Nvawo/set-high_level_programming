#!/usr/bin/python3
"""Unit tests for Rectangle."""
import unittest
from io import StringIO
from unittest.mock import patch

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle class."""

    def test_constructor(self):
        """Test Rectangle constructor."""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_constructor_all_values(self):
        """Test all constructor arguments."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_width_type(self):
        """Test invalid width type."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_height_type(self):
        """Test invalid height type."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_x_type(self):
        """Test invalid x type."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_y_type(self):
        """Test invalid y type."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_width_value(self):
        """Test invalid width values."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_height_value(self):
        """Test invalid height values."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_x_value(self):
        """Test invalid x values."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1)

    def test_y_value(self):
        """Test invalid y values."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 0, -1)

    def test_area(self):
        """Test area."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_str(self):
        """Test string representation."""
        r = Rectangle(4, 6, 2, 3, 10)
        self.assertEqual(str(r), "[Rectangle] (10) 2/3 - 4/6")

    def test_display(self):
        """Test display."""
        r = Rectangle(2, 2)
        with patch("sys.stdout", new=StringIO()) as output:
            r.display()
            self.assertEqual(output.getvalue(), "##\n##\n")

    def test_display_position(self):
        """Test display with x and y."""
        r = Rectangle(2, 2, 1, 1)
        with patch("sys.stdout", new=StringIO()) as output:
            r.display()
            self.assertEqual(output.getvalue(), "\n ##\n ##\n")

    def test_update_args(self):
        """Test update with positional arguments."""
        r = Rectangle(10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        """Test update with keyword arguments."""
        r = Rectangle(10, 10)
        r.update(height=1, width=2, x=3, y=4, id=89)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_to_dictionary(self):
        """Test dictionary representation."""
        r = Rectangle(10, 2, 1, 9, 89)
        expected = {
            "id": 89,
            "width": 10,
            "height": 2,
            "x": 1,
            "y": 9,
        }
        self.assertEqual(r.to_dictionary(), expected)

    def test_create(self):
        """Test create."""
        r = Rectangle.create(
            id=89, width=1, height=2, x=3, y=4
        )
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)


if __name__ == "__main__":
    unittest.main()
