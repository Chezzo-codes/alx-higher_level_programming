#!/usr/bin/python3
"""
This file contains a function that
writes an obj to a text file using
JSON rep
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an obj  to a json file
    """
    with open(filename, "w") as j_file:
        json.dump(my_obj, j_file)
