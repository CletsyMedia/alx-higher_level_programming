#!/usr/bin/python3
"""Contains a function that returns
    an object (Python data structure)
    represented by a JSON string
"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string:
        Args:
            my_str (str): JSON string
        Returns:
            obj: Python data structure
    """
    try:
        return json.loads(my_str)
    except json.JSONDecodeError as e:
        return "[{}] {}".format(e.__class__.__name__, e)
