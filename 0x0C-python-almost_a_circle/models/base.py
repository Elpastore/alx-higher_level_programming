#!/usr/bin/python3
"""
base.py module
"""
import json
import csv


class Base:
    """
    class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization of the class
        Args:
            id(int)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method that serilized the list_dictionaries
        """

        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        method that saves list_objs to a file
        """
        filename = "{:s}.json".format(cls.__name__)

        if list_objs is None:
            list_objs = []

        list_dicts = [obj.to_dictionary() for obj in list_objs]
        saved = cls.to_json_string(list_dicts)

        with open(filename, 'w') as file:
            file.write(saved)

    @staticmethod
    def from_json_string(json_string):
        """
        method that deserialized a json string
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
         returns a list of instances
        """
        import os

        class_name = "{:s}.json".format(cls.__name__)
        if not os.path.isfile(class_name):
            return []
        with open(class_name, 'r') as file:
            list_dicts = cls.from_json_string(file.read())
            return [cls.create(**dictionary) for dictionary in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serialistion in csv"""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                             for obj in list_objs]
            else:
                list_objs = [[obj.id, obj.size, obj.x, obj.y]
                             for obj in list_objs]
        with open(f"{cls.__name__}.csv", "w", newline="",
                  encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialisation from csv
        """
        from models.rectangle import Rectangle
        from models.square import Square
        list_objs = list()
        with open(f"{cls.__name__}.csv", "r", newline="",
                  encoding="utf-8") as file:
            data = csv.reader(file)
            for row in data:
                attrs = [int(element) for element in row]
                if cls is Rectangle:
                    d = {"id": attrs[0], "width": attrs[1], "height": attrs[2],
                         "x": attrs[3], "y": attrs[4]}
                else:
                    d = {"id": attrs[0], "size": attrs[1],
                         "x": attrs[2], "y": attrs[3]}
                list_objs.append(cls.create(**d))
        return list_objs
