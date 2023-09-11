#!/usr/bin/python3

"""
8-rectangle module
"""


class BaseGeometry:
    """Define class"""

    def area(self):
        """area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """_summary_

        Args:
            name (str): string
            value (int): integer

        Raises:
            TypeError: if name is not int
            ValueError: if name is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height) -> None:
        """initialize object
        """

        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
