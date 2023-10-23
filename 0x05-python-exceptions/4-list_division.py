#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            a = my_list_1[i] if i < len(my_list_1) else 0
            b = my_list_2[i] if i < len(my_list_2) else 0

            division = 0

            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                if b != 0:
                    division = a / b
                else:
                    print("division by 0")
            else:
                print("wrong type")

            result.append(division)
        except IndexError:
            print("out of range")

    return result
