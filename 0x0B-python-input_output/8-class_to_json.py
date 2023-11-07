#!/usr/bin/python3
"""a function that returns a dictionary description with simple data structure
  (list, dictionary, string, integer and boolean)for JSON serialization
  of an object
"""


def class_to_json(obj):
    """Returns a dictionary description for JSON serialization of an object
        Args:
            obj: object to serialize
        Returns:
            dict: dictionary description
    """
    return obj.__dict__
