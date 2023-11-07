#!/usr/bin/python3
"""Defines the Student class
"""


class Student:
    """Student class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """Instantiates a Student object with first_name, last_name, and age.
        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.
        Args:
            attrs (list): List of attribute names to include in the dictionary.
        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        filtered_attrs = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_attrs[attr] = getattr(self, attr)
        return filtered_attrs
