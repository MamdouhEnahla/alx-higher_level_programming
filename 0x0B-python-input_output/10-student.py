#!/usr/bin/python3
"""Student Module """


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """ initializatoin """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Converts the Student object to a dictionary (JSON-like representation).
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {x: getattr(self, x) for x in attrs} if attrs
        else:
            return self.__dict__
