#!/usr/bin/python3
def best_score(a_dictionary):
    max_ = 0
    result = ""
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > max_:
                result = k
                max_ = v
        return result
    else:
        return None
