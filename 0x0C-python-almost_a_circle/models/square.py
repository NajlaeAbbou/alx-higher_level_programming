#!/usr/bin/python3
"""the "Square" class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square representation."""

    def __init__(self, size, x=0, y=0, id=None):
        """Init a new Square.
        Args:
            size (int): size of new Square.
            x (int): x coordinate of new Square.
            y (int): y oordinate of  new Square.
            id (int): identity of new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size of Square."""
        return self.width

    @size.setter
    def size(self, value):
        """set size of square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Update square.
        Args:
            *args (ints): New values
            **kwargs (dict): New key=value pairs.
        """
        if args and len(args) != 0:
            p = 0
            for arg in args:
                if p == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif p == 1:
                    self.size = arg
                elif p == 2:
                    self.x = arg
                elif p == 3:
                    self.y = arg
                p += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """dictionary representation of Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
