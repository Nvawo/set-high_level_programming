
#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_id_none(self):
        """Test automatic ID assignment."""
        base = Base()
        self.assertIsInstance(base.id, int)

    def test_id_integer(self):
        """Test Base with an integer ID."""
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_id_string(self):
        """Test Base with a string ID."""
        base = Base("10")
        self.assertEqual(base.id, "10")

    def test_id_zero(self):
        """Test Base with ID zero."""
        base = Base(0)
        self.assertEqual(base.id, 0)

    def test_id_negative(self):
        """Test Base with a negative ID."""
        base = Base(-5)
        self.assertEqual(base.id, -5)


if __name__ == "__main__":
    unittest.main()
