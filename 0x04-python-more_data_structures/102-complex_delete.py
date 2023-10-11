#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    return {k: v for k, v in a_dictionary.items() if v != value}
