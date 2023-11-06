#!/usr/bin/python3
""" Module that returns a list of available
    attributes and methods of an object:
"""


def lookup(obj):
  """
    Args:
        obj: The object for which you want to retrieve the attributes and methods.

    Returns:
        A list of strings containing the names of attributes and methods associated with the object.

    Example:
        >>> class MyClass:
        ...     def __init__(self):
        ...         self.attribute = 42
        ...     def method(self):
        ...         pass
        ...
        >>> lookup(MyClass())
        ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge',
        '__getattribute__', '__gt', '__hash__', '__init__', '__le', '__lt', '__ne', '__new', '__reduce',
        '__reduce_ex', '__repr', '__setattr', '__sizeof', '__str', '__subclasshook', '__weakref',
        'attribute', 'method']
    """
  return dir(obj)
