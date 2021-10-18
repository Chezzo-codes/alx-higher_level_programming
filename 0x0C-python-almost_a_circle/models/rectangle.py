#!/usr/bin/python3
"""
Module contains class Rectangle which inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle containing private instance
    attributes __width,  __height, __x and __y
    and a class constructor
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialise instances
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Validation and Setter for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter height
        """
        return self.__width

    @height.setter
    def height(self, value):
        """
        Validation and Setter for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        Getter x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Validation and Setter for x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0 ")
        else:
            self.__x = value

    @property
    def y(self):
        """
        Getter y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Validation and Setter for y
        """
        if type(value) is not int:
            raise TypeError("y mut be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Returns the area of a rectangle instance
        """
        return (self.__width * self.__height)

    def display(self):
        """
        prints in stdout the Rectangle
        instance with the character #
        """
        for h in range(self.__height):
            print("#" * self.__width)
