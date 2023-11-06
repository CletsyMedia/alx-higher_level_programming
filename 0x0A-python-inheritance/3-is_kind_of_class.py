#!/usr/bin/python3

"""Module checks if an object is an instance of a
class or of an inherited class
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance or inherited from the class, otherwise False.
    """
    
    return True if isinstance(obj, a_class) else False
