#!/usr/bin/python3

"""A module of a model class bass"""

import json
import csv
import turtle


class Base:
    """Base class

    Private class attribute:
        __nb_objects (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the attributes of the instance.

        Args:
            id (int): The identity
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON of a list of dictionary.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dicts = [f.to_dictionary() for f in list_objs]
                json_file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string.

        Args:
            json_string (str): A JSON string.
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set.

        Args:
            **dictionary (dict): double pointer to a dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_dict = cls(1, 1)
            else:
                new_dict = cls(1)
            new_dict.update(**dictionary)
            return new_dict

    @classmethod
    def load_from_file(cls):
        """Method that  that returns a list of instances."""
        try:
            with open("{}.json".format(cls.__name__), "r") as file:
                json_data = file.read()
                data = cls.from_json_string(json_data)
                return [cls.create(**obj) for obj in data]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """A mehod that serializes CSV.

        Args:
            list_objs (list): A list of inherited base instance.
        """
        with open("{}.csv".format(cls.__name__), "w", newline="") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """a method that deserializes in CSV"""
        try:
            with open(
                    "{}.csv".format(cls.__name__),
                    "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csv_file, fieldnames=fieldnames)
                list_dicts = [
                        dict([k, int(v)] for k, v in d.items())
                        for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """A module that draws rectangle and square.

        Args:
            list_rectangles (list): A list of rectangle
            list_squares (list): A list of square
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rec in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rec.x, rec.y)
            turt.down()
            for i in range(2):
                turt.showturtle()
                turt.up()
                turt.goto(sq.x, sq.y)
                turt.down()
                for i in range(2):
                    turt.forward(sq.width)
                    turt.left(90)
                    turt.forward(sq.height)
                    turt.left(90)
                turt.hideturtle()

            turtle.exitonclick()
