#!/usr/bin/python3
"""
Define a square and validate size
"""


class Square:
    """
    Args:
        size: size of the square
    """
    def __init__(self, size=0):
        """
        Initialise square and raise errors
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
