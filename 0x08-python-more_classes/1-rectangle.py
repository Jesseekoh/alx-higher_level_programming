#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """defines a rectangle"""
    def __init__(self, width=0, height=0) -> None:
        """Initializes a Rectangle

        Args:
            width (int, optional): Width of the new rectangle. Defaults to 0.
            height (int, optional): height of the new rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
