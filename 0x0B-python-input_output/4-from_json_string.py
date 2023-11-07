#!/usr/bin/python3
"""
returns an object represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
        returns an object represented by a JSON string
    """
    try:
        return json.loads(my_str)
    except json.JSONDecodeError as e:
        return "[{}] {}".format(e.__class__.__name__, e)
