#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 'z')
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = -2
print(my_rectangle.__dict__)
