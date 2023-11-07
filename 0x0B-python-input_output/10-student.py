#!/usr/bin/python3
"""
10-student module"
"""


class Student:
    """
    Class of Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialisation of the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve a dictionnary
            same as 8-class_to_json
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {x: y for x, y in self.__dict__.items() if x in attrs}
        else:
            return self.__dict__
