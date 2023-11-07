#!/usr/bin/python3
"""
9-student module"
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

    def to_json(self):
        """retrieve a dictionnary
            same as 8-class_to_json
        """
        return self.__dict__
