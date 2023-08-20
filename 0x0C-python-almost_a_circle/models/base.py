#!/usr/bin/python3
"""base model class"""


class Base:
    """Base model representation
    Args:
        __nb_object (int): Number of inst Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Init new Base

        Args:
            id (int): identit
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

