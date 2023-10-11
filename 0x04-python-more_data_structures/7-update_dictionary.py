#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    updated = False  # Flag to track whether the key was updated or added
    for k in a_dictionary:
        if k == key:
            a_dictionary[k] = value  # Update the value if the key exists
            updated = True
    if not updated:
        a_dictionary[key] = value  # Add the key and value if it doesn't exist
    return a_dictionary
