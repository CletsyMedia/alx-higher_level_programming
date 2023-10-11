#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_add = set()  # Create a set to store unique integers
    sum = 0  # Initialize the total sum to zero
    # Iterate through the list
    for num in my_list:
       # Check if the integer is not in the set
        if num not in unique_add:
           # Add the unique integer to the set
            unique_add.add(num)
            # Add the unique integer to the sum num
            sum += num
    return sum
