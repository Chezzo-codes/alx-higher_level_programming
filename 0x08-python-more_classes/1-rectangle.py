#!/usr/bin/python3
"""
Module defines properties of a rectangle
"""


class Rectangle:
    """
    Rectangle Class
    """
    def __init__(self, width=0, height=0):
        """
        Initialize objects
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter (width)
        """
        return self.__width

    @width.setter
    def width(self, val):
        """
        Setter (width)
        """
        if isinstance(val, int) is False:
            raise TypeError("width must be an integer")
        elif val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        """
        Getter (height)
        """
        return self.__height

    @height.setter
    def height(self, val):
        """
        Setter (height)
        """
        if isinstance(val, int) is False:
            raise TypeError("height must be an integer")
        elif val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val
