#!/usr/bin/python3
"""
Module contains definition of class Base
with attributes and methods
"""


class Base:
    """
    Class Base with private attribute __nb_objects = 0
    and constructor definition to check for id.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize instances
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objectss += 1
            self.id = Base.__nb_objects
