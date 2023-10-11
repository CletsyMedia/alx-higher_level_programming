#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set from the list to automatically remove duplicates
    unique_set = set(my_list)
    # Use the sum function to add all unique integers
    total = sum(unique_set)
   # Return the sum of unique integers
    return total
