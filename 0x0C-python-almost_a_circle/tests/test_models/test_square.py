#!/usr/bin/python3
"""Module for Square unit tests"""
import unittest
import io
import sys
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_size_validation(self):
        """
        test fir size value
        """
        with self.assertRaises(TypeError):
            s = Square("invalid")
        with self.assertRaises(ValueError):
            s = Square(-5)

    def test_init(self):
        """
        test for iniatialisation
        """
        Base._Base__nb_objects = 0

        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)

        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.area(), 25)

        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.area(), 4)

        self.assertEqual(s3.size, 3)
        self.assertEqual(s3.area(), 9)

    def test_print_area(self):
        """
        test for print area
        """
        saved_output = sys.stdout
        sys.stdout = io.StringIO()

        s1 = Square(5)
        s1.display()
        expect_output = "#####\n#####\n#####\n#####\n#####\n"

        actual_output = sys.stdout.getvalue()
        self.assertEqual(expect_output, actual_output)
        sys.stdout = saved_output

        saved_output = sys.stdout
        sys.stdout = io.StringIO()

        s2 = Square(2, 2)
        s2.display()
        expect_output = "  ##\n  ##\n"

        actual_output = sys.stdout.getvalue()
        self.assertEqual(expect_output, actual_output)
        sys.stdout = saved_output

        saved_output = sys.stdout
        sys.stdout = io.StringIO()

        s3 = Square(3, 1, 3)
        s3.display()
        expect_output = "\n\n\n ###\n ###\n ###\n"

        actual_output = sys.stdout.getvalue()
        self.assertEqual(expect_output, actual_output)
        sys.stdout = saved_output

    def test_to_dictionary(self):
        """
        test for dictionary
        """
        s = Square(1, 2, 3, 4)
        expected_dict = {'id': 4, 'size': 1, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)

        s.update(5, 6, 7, 8)
        self.assertEqual(s.to_dictionary(), {'id': 5, 'size': 6, 'x': 7, 'y': 8})
        self.assertEqual(type(s.to_dictionary()), dict)

    def test_str(self):
        """
        test for _str_
        """
        s = Square(1, 2, 3, 4)
        expected_output = "[Square] (4) 2/3 - 1"
        self.assertEqual(str(s), expected_output)


if __name__ == '__main__':
    unittest.main()
