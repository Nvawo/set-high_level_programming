#!/usr/bin/python3
"""Unit tests for Square."""
import unittest

from models.square import Square


class TestSquare(unittest.TestCase):
    """Test Square class."""

    def test_constructor(self):
        """Test Square constructor."""
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_constructor_all_values(self):
        """Test all constructor arguments."""
        s = Square(5, 2, 3, 10)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_size_type(self):
        """Test invalid size."""
        with self.assertRaises(TypeError):
            Square("1")

    def test_size_value(self):
        """Test invalid size values."""
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-1)

    def test_x_type(self):
        """Test invalid x."""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_type(self):
        """Test invalid y."""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_str(self):
        """Test string representation."""
        s = Square(5, 2, 3, 10)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 5")

    def test_update_args(self):
        """Test update with positional arguments."""
        s = Square(5)
        s.update(89, 2, 3, 4)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test update with keyword arguments."""
        s = Square(5)
        s.update(id=89, size=2, x=3, y=4)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_to_dictionary(self):
        """Test dictionary representation."""
        s = Square(10, 2, 1, 89)
        expected = {
            "id": 89,
            "size": 10,
            "x": 2,
            "y": 1,
        }
        self.assertEqual(s.to_dictionary(), expected)

    def test_create(self):
        """Test create."""
        s = Square.create(id=89, size=1, x=2, y=3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)


if __name__ == "__main__":
    unittest.main()
    def test_negative_y(self):
        """Test negative y."""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_save_to_file_none(self):
        """Test save_to_file with None."""
        Square.save_to_file(None)
        with open("Square.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty(self):
        """Test save_to_file with an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_objects(self):
        """Test save_to_file with Square objects."""
        square = Square(1)
        Square.save_to_file([square])

        with open("Square.json", "r", encoding="utf-8") as file:
            data = file.read()

        self.assertIn('"size": 1', data)

    def test_load_from_file_missing(self):
        """Test load_from_file when the file does not exist."""
        import os

        if os.path.exists("Square.json"):
            os.remove("Square.json")

        squares = Square.load_from_file()
        self.assertEqual(squares, [])

    def test_load_from_file_exists(self):
        """Test load_from_file when the file exists."""
        square = Square(1)
        Square.save_to_file([square])

        squares = Square.load_from_file()

        self.assertEqual(len(squares), 1)
        self.assertIsInstance(squares[0], Square)
        self.assertEqual(squares[0].size, 1)
