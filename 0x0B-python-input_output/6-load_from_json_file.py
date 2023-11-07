#!/usr/bin/python3
"""a function that creates an Object from a JSON file"""

import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file:
        Args:
            filename (str): name of the file
        Returns:
            object: Python data structure loaded from the JSON file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None
