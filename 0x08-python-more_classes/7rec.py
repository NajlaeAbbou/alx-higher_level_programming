#!/usr/bin/python3
"""Empty class that defines a Rectangle"""


class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """The area of the Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """The perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        string = []
        for i in range(self.__height):
            [string.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                string.append("\n")
        return ("".join(string))

    def __repr__(self):
        """The string representation"""
        string = "Rectangle(" + str(self.__width)
        string += ", " + str(self.__height) + ")"
        return (string)

    def __del__(self):
        """Print Bye rectangle when a Rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
