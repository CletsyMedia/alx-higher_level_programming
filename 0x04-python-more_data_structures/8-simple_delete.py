#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        for k in list(a_dictionary):
            if k == key:
                del a_dictionary[k]
    return a_dictionary
