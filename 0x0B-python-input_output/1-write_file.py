#!/usr/bin/python3
"""Contains function that writes a
string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Write a string to a text file and return the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written.

    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
