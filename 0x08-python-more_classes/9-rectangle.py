#!/usr/bin/python3
'''a class Rectangle that defines a rectangle'''


class Rectangle:
    '''define a class Rectangle.

    Field:
        number_of_instances (int): The num of rectangle object.
        print_symbol (symbol): Symbol for string representation
    '''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Initialize the attribute of the new rectangle.

        Args:
            width (int): The width of new Rectangle
            height (int): The height of the new Rectangle
        '''
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''that returns the biggest rectangle based on the area.
        Args:
            rect_1 (Rectengle): The first Rectangle
            rect_2 (Rectangle): The second Rectangle
        Raises:
            TypeError: If either of rect_1 or Rect_2 is not a Rectangle.
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        ''' returns a new Rectangle instance with width == height == size.
        Args:
            size (int): The width and height of the new Rectangle.
        '''
        return (cls(size, size))

    def __str__(self):
        '''method to print the rectangle with the character #'''
        if self.__width == 0 or self.__height == 0:
            return ("")
        rec_t = []

        for i in range(self.__height):
            [rec_t.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rec_t.append('\n')
        return ("".join(rec_t))

    def __repr__(self):
        '''Return the string representation of the new rectangle'''
        rec_t = "Rectangle(" + str(self.__width)
        rec_t += ", " + str(self.__height) + ")"
        return (rec_t)

    def __del__(self):
        '''Print the message Bye rectangle...
            when an instance of Rectangle is deleted
        '''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
