#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """class with public instance methods"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """if value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
