#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class for test_list
    """
    def test_max(self):
        """
        Method that test the max int in a list
        """
        result = max_integer([3, 4, 5, 6, 3, 4, 5, 6, 9])
        self.assertEqual(result, 9)

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_syngle(self):
        self.assertEqual(max_integer([8]), 8)

    def test_neg(self):
        self.assertEqual(max_integer([-1, -3, -4, -2, -5]), -1)

    def test_pos_neg(self):
        self.assertEqual(max_integer([3, -1, 2, -3, 4, -2, -5, 9]), 9)

    def test_float(self):
        self.assertEqual(max_integer([2.4, 3.5, 3.9, 4, 5.5]), 5.5)

    def test_same(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_strings(self):
        self.assertEqual(max_integer("hello"), "o")
        self.assertEqual(max_integer("Abdoulaye"), "y")
        self.assertEqual(max_integer("AbdoulaYe"), "u")
        self.assertEqual(max_integer(['h', 'e', 'l', 'l', 'o']), "o")

    def test_mix(self):
        mix = [1, 4, 5, "Abdoulaye", 24]
        with self.assertRaises(TypeError):
            max_integer(mix)


if __name__ == "__main__":
    unittest.main()
