#!#/usr/bin/python3
"""
File with function which takes an object and converts it to json
"""
import json


def to_json_string(my_obj):
    """
    Returns a string of json data
    """
    j_data = json.dumps(my_obj)
    return j_data
