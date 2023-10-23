#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        printed = 0
        for i in my_list:
            if printed < x:
                print(i, end="")
                printed += 1
        print()
        return printed
    except TypeError:
        pass
