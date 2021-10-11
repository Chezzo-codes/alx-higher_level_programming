#!/usr/bin/python3
"""
Module with function that looks up attributes available for an object
"""


def lookup(obj):
    """
    Returns all available attributes of obj
    """
    return dir(obj)
