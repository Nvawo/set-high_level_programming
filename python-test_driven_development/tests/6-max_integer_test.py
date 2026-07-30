#!/usr/bin/python3
"""Unit tests for max_integer()."""

import unittest
import importlib.util
import os

# Load 6-max_integer.py
module_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "6-max_integer.py"
)

spec = importlib.util.spec_from_file_location(
    "max_integer_module",
    module_path
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
max_integer = module.max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer())

    def test_single_element(self):
        """Test a list with one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_sorted_list(self):
        """Test an ascending list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        """Test an unsorted list."""
        self.assertEqual(max_integer([4, 2, 8, 1, 6]), 8)

    def test_negative_numbers(self):
        """Test negative integers."""
        self.assertEqual(max_integer([-8, -5, -2, -9]), -2)

    def test_mixed_numbers(self):
        """Test positive and negative integers."""
        self.assertEqual(max_integer([-10, 5, 0, 3]), 5)

    def test_max_at_beginning(self):
        """Test when max is first."""
        self.assertEqual(max_integer([9, 4, 3, 2]), 9)

    def test_max_at_end(self):
        """Test when max is last."""
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_duplicate_max(self):
        """Test duplicate maximum values."""
        self.assertEqual(max_integer([5, 3, 5, 2]), 5)

    def test_float_values(self):
        """Test float values."""
        self.assertEqual(max_integer([1.2, 7.8, 3.4]), 7.8)

    def test_string_values(self):
        """Test string values."""
        self.assertEqual(max_integer(["a", "z", "m"]), "z")


if __name__ == "__main__":
    unittest.main()
