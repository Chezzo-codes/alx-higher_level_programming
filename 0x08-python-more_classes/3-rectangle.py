#!/usr/bin/python3
"""
Module defines properties of a rectangle.
"""


class Rectangle:
    """
    Rectangle Class with width and heightt
    """
    def __init__(self, width=0, height=0):
        """
        Initialize dimensions
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter width
        """
        return self.__width

    @width.setter
    def width(self, val):
        """
        Setter width
        """
        if isinstance(val, int) is False:
            raise TypeError("width must be an integer")
        elif val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        """
        Getter height
        """
        return self.__height

    @height.setter
    def height(self, val):
        """
        Setter height
        """
        if isinstance(val, int) is False:
            raise TypeError("height must be an integer")
        elif val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        0 if height or width is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        returns string of rectangle made up of '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            width = "#" * self.__width
            rectangle = (width + '\n') * self.__height
            return rectangle
