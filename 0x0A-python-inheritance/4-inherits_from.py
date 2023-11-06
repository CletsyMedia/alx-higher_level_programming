#!/usr/bin/python3

"""Check if an object is an instance of a class that inherited
   (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of an inherited class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

