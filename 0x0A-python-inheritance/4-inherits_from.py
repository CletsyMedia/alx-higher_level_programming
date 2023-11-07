#!/usr/bin/python3
"""Module that determines if an object is an instance of a
class that inherited from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj (obj): The object to check.
        a_class (obj): The class to compare against.

    Returns:
        bool: True if the object is an instance of an inherited class, otherwise False.
    """

    return True if isinstance(obj, a_class) and \
        type(obj) is not a_class else False

