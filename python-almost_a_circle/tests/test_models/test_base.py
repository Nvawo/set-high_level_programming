#!/usr/bin/python3
"""Unit tests for Base."""
import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """Test Base class."""

    def test_id_none(self):
        """Test automatic ID assignment."""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base2.id, base1.id + 1)

    def test_id_given(self):
        """Test supplied ID."""
        base = Base(89)
        self.assertEqual(base.id, 89)

    def test_to_json_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_empty(self):
        """Test to_json_string with empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_dictionary(self):
        """Test dictionary conversion."""
        result = Base.to_json_string([{"id": 12}])
        self.assertEqual(result, '[{"id": 12}]')

    def test_to_json_returns_string(self):
        """Test JSON result type."""
        result = Base.to_json_string([{"id": 12}])
        self.assertIsInstance(result, str)

    def test_from_json_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_empty(self):
        """Test from_json_string with empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_data(self):
        """Test from_json_string with JSON data."""
        result = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(result, [{"id": 89}])

    def test_from_json_returns_list(self):
        """Test from_json_string result type."""
        result = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()
