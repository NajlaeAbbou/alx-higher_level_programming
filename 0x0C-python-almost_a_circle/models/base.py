#!/usr/bin/python3
"""base model class."""
import json
import csv
import turtle


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON representation of a list of dictionnary.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON representation of a list to file.
        Args:
            cls : file name.
            list_objs (list): A list instances from base.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Representation of a JSON string.
        Args:
            json_string (str): list of dicts.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set.
        Args:
            cls : filename
            **dictionary (dict): Key=value pairs of attributes
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                cre = cls(1, 1)
            else:
                cre = cls(1)
            cre.update(**dictionary)
            return cre

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """deserialize in CSV"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=field_names)
                list_dicts = [dict([k, int(v)] for k, v in dic.items())
                              for dic in list_dicts]
                return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialise a CSV file.
        Args:
            list_objs (list): A list of instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares.
        Args:
            list_rectangles (list): params of Rectangle
            list_squares (list): params of Square
        """
        param = turtle.Turtle()
        param.screen.bgcolor("#8fce00")
        param.pensize(3)
        param.shape("turtle")

        param.color("#444444")
        for rec in list_rectangles:
            param.showturtle()
            param.up()
            param.goto(rect.x, rec.y)
            param.down()
            for i in range(2):
                param.forward(rec.width)
                param.left(90)
                param.forward(rec.height)
                param.left(90)
            param.hideturtle()

        param.color("#e69138")
        for squ in list_squares:
            param.showturtle()
            param.up()
            param.goto(squ.x, squ.y)
            param.down()
            for i in range(2):
                param.forward(squ.width)
                param.left(90)
                param.forward(squ.height)
                param.left(90)
            param.hideturtle()

        turtle.exitonclick()
