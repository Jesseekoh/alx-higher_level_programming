#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width of rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
