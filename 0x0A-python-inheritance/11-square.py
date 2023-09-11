#!/usr/bin/python3
"""10-square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Doc"""
    def __init__(self, size):
        """initialize object"""
        super().integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """str"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
