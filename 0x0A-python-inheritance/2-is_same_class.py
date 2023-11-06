#!/usr/bin/python3
"""Module has a functction that checks if an object is an instance
  or a specified class
"""
def is_same_class(obj, a_class):
    """
    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance, otherwise False.
    """
    return type(obj) == a_class
