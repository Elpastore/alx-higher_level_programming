#!/usr/bin/python3
"""Module for Base unit tests."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):

    def setup(self):
        """
        reset the class counter before each test
        """
        Base._Base__nb_objects = 0
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

    def test_to_json_string(self):

        Base._Base__nb_objects = 0
        input_list = [{"id": 1, "width": 2, "height": 3}, {"id": 2, "width": 4, "height": 5}]
        expected_output = '[{"id": 1, "width": 2, "height": 3}, {"id": 2, "width": 4, "height": 5}]'
        input_list_2 = []

        self.assertEqual(Base.to_json_string(input_list), expected_output)
        self.assertEqual(Base.to_json_string(input_list_2), '[]')

        self.assertEqual(Base.to_json_string(None), "[]")

        self.assertEqual(type(input_list), list)
        with self.assertRaises(NameError):
            Base.to_json_string(input_list_3)

    def test_save_to_file(self):

        filename = "Rectangle.json"
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        Rectangle.save_to_file([r1, r2])

        self.assertTrue(os.path.isfile(filename))

        loaded_rectangles = Rectangle.load_from_file()

        self.assertEqual(len(loaded_rectangles), 2)
        self.assertEqual(loaded_rectangles[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(loaded_rectangles[1].to_dictionary(), r2.to_dictionary())


if __name__ == '__main__':
    unittest.main()
