#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0.0

    total_score = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)

    return total_score / total_weight
