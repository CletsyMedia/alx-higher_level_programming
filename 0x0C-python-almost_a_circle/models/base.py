#!/usr/bin/python3
"""Module for creating Base class"""
from json import dumps, loads
import csv
from turtle import Turtle, Screen  # Import Turtle graphics module


class Base:
    """This represents the base class of OOP hierarchical classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        filename = "{}.json".format(cls.__name__)
        with open(filename, mode='w') as file:
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries represented by json_string"""
        if not json_string or json_string == "[]":
            return []
        return loads(json_string)

    @classmethod
    def create(cls, *args, **dictionary):
        """Return an instance with all attributes set from the dictionary"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a dummy Square instance

        if args:
            dummy_instance.update(*args)
        else:
            dummy_instance.update(**dictionary)  # Update the dummy instance with real values

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from the JSON file"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, mode='r') as file:
                json_string = file.read()
                dict_list = cls.from_json_string(json_string)
                return [cls.create(**item) for item in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV representation of list_objs to a file"""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances from the CSV file"""
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                return [cls.create(*map(int, row)) for row in reader]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw all the Rectangles and Squares using Turtle graphics module"""
        screen = Screen()
        screen.bgcolor("white")
        screen.title("Turtle Drawing")

        # Draw Rectangles
        for rect in list_rectangles:
            turtle = Turtle()
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)

        # Draw Squares
        for square in list_squares:
            turtle = Turtle()
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

        screen.mainloop()
