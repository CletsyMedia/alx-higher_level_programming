#!/usr/bin/python3
def non_common_elements(set_1, set_2):
    unique_to_set_1 = set_1 - set_2
    unique_to_set_2 = set_2 - set_1
    result = unique_to_set_1 | unique_to_set_2
    return sorted(list(result))
