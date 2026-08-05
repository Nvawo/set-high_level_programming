#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest

from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for Square."""

    def test_size(self):
        """Test size through width and height."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_id(self):
        """Test ID."""
        s = Square(5, id=89)
        self.assertEqual(s.id, 89)

    def test_position(self):
        """Test x and y."""
        s = Square(5, 2, 3)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_area(self):
        """Test square area."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        """Test string representation."""
        s = Square(5, 2, 3, 89)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 5")

    def test_inherits_rectangle(self):
        """Test inheritance from Rectangle."""
        s = Square(5)
        self.assertIsInstance(s, Square)
        self.assertTrue(hasattr(s, "width"))
        self.assertTrue(hasattr(s, "height"))
        self.assertTrue(hasattr(s, "x"))
        self.assertTrue(hasattr(s, "y"))

    def test_invalid_size(self):
        """Test invalid size."""
        with self.assertRaises(TypeError):
            Square("5")

        with self.assertRaises(ValueError):
            Square(0)

        with self.assertRaises(ValueError):
            Square(-5)

    def test_invalid_x(self):
        """Test invalid x."""
        with self.assertRaises(TypeError):
            Square(5, "2")

        with self.assertRaises(ValueError):
            Square(5, -2)

    def test_invalid_y(self):
        """Test invalid y."""
        with self.assertRaises(TypeError):
            Square(5, 0, "3")

        with self.assertRaises(ValueError):
            Square(5, 0, -3)


if __name__ == "__main__":
    unittest.main()
