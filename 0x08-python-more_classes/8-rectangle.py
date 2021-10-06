#!/usr/bin/python3
"""
Module defines properties of a Rectangle.
"""


class Rectangle:
    """
    Rectangle with width and height as args.
    Keeps track of number of instances.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize rectangle object
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        if not isinstance(val, int):
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
        Returns string of rectangle made up of '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        sy = str(self.print_symbol)
        return ((sy*self.__width + "\n")*self.__height)[:-1]

    def __repr__(self):
        """
        Returns the class representation as a string
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        Prints message when rect is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            compare 2 rectangle
        Args:
            rect_1(Rectangle): First Rectangle
            rect_2(Rectangle): Second Rectangle
        Raises:
            TypeError: If rect_1 is not instance of Rectangle
            TypeError: If rect_2 is not instance of rectangle
        Return:
            Biggest Rectangle (Rectangle)
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        Area1 = rect_1.area()
        Area2 = rect_2.area()
        if Area1 >= Area2:
            return rect_1
        return rect_2
