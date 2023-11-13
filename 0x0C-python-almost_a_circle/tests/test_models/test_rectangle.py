#!/usr/bin/python3
"""
test module for Rectangle
"""
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test for class rectangle
    """
    def test_id(self):
        """
        test for id
        """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(3, 4)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r4.id, 3)

    def test_width_height(self):
        """
        test for width and height value
        """
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 5)
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 5)

        with self.assertRaises(TypeError):
            r = Rectangle(2, '6')
        with self.assertRaises(ValueError):
            r = Rectangle(1, -3)

        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(3, 4)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)

        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)

        self.assertEqual(r4.width, 3)
        self.assertEqual(r4.height, 4)

    def test_x_y(self):
        """
        test for x and y value
        """
        r = Rectangle(1, 1, 2, 3)

        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        with self.assertRaises(TypeError):
            r.x = "invalid"
        with self.assertRaises(ValueError):
            r.y = -5

        with self.assertRaises(TypeError):
            r.y = "invalid"
        with self.assertRaises(ValueError):
            r.x = -5

    def test_area(self):
        """
        test for area
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(5, 3, 0, 0, 12)
        r4 = Rectangle(3, 4)

        self.assertEqual(r1.area(), 20)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 15)
        self.assertEqual(r4.area(), 12)

    def test_display(self):
        """test for display method"""
        saved_output = sys.stdout
        sys.stdout = io.StringIO()

        r = Rectangle(3, 2)
        r.display()
        expected_output = "###\n###\n"

        actual_output = sys.stdout.getvalue()
        self.assertEqual(actual_output, expected_output)
        sys.stdout = saved_output

    def test_display_2(self):
        """
        test 2 for display
        """
        saved_output = sys.stdout
        sys.stdout = io.StringIO()

        r = Rectangle(5, 6, 7, 8)
        r.display()
        expected_output = """







       #####
       #####
       #####
       #####
       #####
       #####
"""

        actual_output = sys.stdout.getvalue()
        self.assertEqual(actual_output, expected_output)
        sys.stdout = saved_output

    def test_print(self):
        """
        test for str method
        """
        Base._Base__nb_objects = 0
        r2 = Rectangle(4, 6, 2, 1)
        print_r2 = "[Rectangle] (1) 2/1 - 4/6"
        self.assertEqual(str(r2), print_r2)

        r1 = Rectangle(4, 6, 2, 1, 12)
        print_r1 = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), print_r1)

        r3 = Rectangle(4, 6, 2)
        print_r3 = "[Rectangle] (2) 2/0 - 4/6"
        self.assertEqual(str(r3), print_r3)

        r4 = Rectangle(4, 6)
        print_r4 = "[Rectangle] (3) 0/0 - 4/6"
        self.assertEqual(str(r4), print_r4)

    def test_update(self):
        """
        test for updated
        """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        r1_dictionary = r1.to_dictionary()
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        r2 = Rectangle(2, 2)
        r2.update(**r1_dictionary)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 10/10 - 10/10")

    def test_dictionary(self):
        """
        test for dictionary
        """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()

        expected = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1_dictionary, expected)
        self.assertEqual(type(r1_dictionary), dict)

        r = Rectangle(1, 2, 3, 4, 5)
        r.update(6, 7, 8, 9, 10)
        self.assertEqual(r.to_dictionary(), {'id': 6, 'width': 7, 'height': 8, 'x': 9, 'y': 10})


if __name__ == '__main__':
    unittest.main()
