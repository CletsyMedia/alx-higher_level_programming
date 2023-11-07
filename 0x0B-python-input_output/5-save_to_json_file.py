#!/usr/bin/python3
"""function that writes an Object to a
    text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using a JSON representation:
        Args:
            my_obj: object to be saved
            filename (str): name of the file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
