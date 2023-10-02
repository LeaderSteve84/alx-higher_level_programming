#!/usr/bin/python3
'''a class Rectangle that defines a rectangle'''


class Rectangle:
    '''define a class Rectangle'''

    def __init__(self, width=0, height=0):
        '''Initialize the attribute of the new rectangle.

        Args:
            width (int): The width of new Rectangle
            height (int): The height of the new Rectangle
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''retrieve the width of new rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set the value of the new rectangle.

        Agrs:
            value (int): value of width.
        '''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''retrieve the height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set the value of the new rectangle.

        Args:
            value (int): The value of the height
        '''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''retieve the area of the new rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''retrieve the perimeter of the new rectangle'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
