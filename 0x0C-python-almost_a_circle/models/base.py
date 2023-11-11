#!/usr/bin/python3
"""Module for creating Base class"""
from json import dumps, loads
import csv


class Base:
  """This represent the base class of OOP hierarchical classes"""
  
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
  def create(cls, **dictionary):
      """Return an instance with all attributes set from the dictionary"""
      if cls.__name__ == "Rectangle":
        dummy_instance = cls(1, 1)  # Create a dummy Rectangle instance
      elif cls.__name__ == "Square":
          dummy_instance = cls(1)  # Create a dummy Square instance

      dummy_instance.update(**dictionary)  # Update the dummy instance with real values
      return dummy_instance
    
