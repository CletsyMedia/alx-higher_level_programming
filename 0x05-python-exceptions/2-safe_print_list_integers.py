#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if i >= len(my_list):
                raise IndexError  # Raise IndexError if x exceeds the list length
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()
    except (ValueError, TypeError):
        pass
    except IndexError:
        raise  # Re-raise the IndexError to show the error message

    return count
