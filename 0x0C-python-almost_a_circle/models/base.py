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

