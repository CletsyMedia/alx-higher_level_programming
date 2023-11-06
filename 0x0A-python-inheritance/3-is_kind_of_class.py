#!/usr/bin/python3
"""Check if the object is an instance of, or if it's an instance of a class
   that inherited from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance or inherited from the class, otherwise False.
    """
    return isinstance(obj, a_class)
