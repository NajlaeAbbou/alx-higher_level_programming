#!/usr/bin/python3
"""rectangle class."""
from models.base import Base


class Rectangle(Base):
    """rectangle representation"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init a new Rectangle

        Args:
            width (int): width of Rectangle
            height (int): height of Rectangle
            x (int): x coordinate of Rectangle
            y (int): y oordinate of Rectangle
            id (int): identity
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x coordinate"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y oordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y oordinate"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area width*height."""
        return self.width * self.height

    def display(self):
        """Print Rectangle using `#`"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for hei in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for wid in range(self.width)]
            print("")

    def __str__(self):
        """Return the print() and str."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
