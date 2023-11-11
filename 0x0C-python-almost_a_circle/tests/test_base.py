#!/usr/bin/python3
"""Module for Base unit tests."""
import unittest
from models.base import Base

class Test_Base(unittest.TestCase):

    def test_initialization_with_id(self):
        obj = Base(id=42)
        self.assertEqual(obj.id, 42)

    def test_initialization_without_id(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        obj4 = Base()
        obj5 = Base()
        obj6 = Base()
        obj7 = Base(24)
        obj8 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)
        self.assertEqual(obj4.id, 4)
        self.assertEqual(obj5.id, 5)
        self.assertEqual(obj6.id, 6)
        self.assertEqual(obj7.id, 24)
        self.assertEqual(obj8.id, 7)

if __name__ == '__main__':
    unittest.main()
