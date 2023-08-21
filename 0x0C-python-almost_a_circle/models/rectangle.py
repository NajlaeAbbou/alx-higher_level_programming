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

    def display(self):
        """Print Rectangle using `#`."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for hei in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for wid in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update Rectangle.
        Args:
            *args : New params
            **kwargs : New key=value pairs.
        """
        if args and len(args) != 0:
            p = 0
            for arg in args:
                if p == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif p == 1:
                    self.width = arg
                elif p == 2:
                    self.height = arg
                elif p == 3:
                    self.x = arg
                elif p == 4:
                    self.y = arg
                p += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
            """dictionary representation of Rectangle."""
            return {
                    "id": self.id,
                    "width": self.width,
                    "height": self.height,
                    "x": self.x,
                    "y": self.y
                    }
