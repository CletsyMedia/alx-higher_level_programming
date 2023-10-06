#!/usr/bin/python3
# Check if 'idx' is out of valid range
# and if so, return the original 'my_list'.
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):  # Check if 'idx' is invalid.
        return my_list
    else:
        my_list[idx] = element
        return my_list
