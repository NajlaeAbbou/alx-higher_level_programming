#!/usr/bin/python3
"""class Student"""


class Student:
    """student"""
    def __init__(self, first_name, last_name, age):
        """Init the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary of Student instance"""
        return self.__dict__
