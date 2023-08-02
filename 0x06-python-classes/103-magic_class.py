#!/usr/bin/python3
import math

class MagicClass:
    """This represents a circle"""
    def __init__(self, radius=0):
        """Initializes the Magic Class"""
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    @property
    def radius(self):
        """Getter method for the radius attribute"""
        return self.__radius

    def area(self):
        """Calculates the area of the circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates the circumference of the circle"""
        return 2 * math.pi * self.__radius
