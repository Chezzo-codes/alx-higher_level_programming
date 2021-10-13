#!/usr/bin/python3
"""
Contains a function that returns
an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    returns python object from json string
    """
    json_data = json.loads(my_str)
    return json_data
