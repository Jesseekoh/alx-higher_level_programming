#!/usr/bin/python3

"""7-base_geometry module"""


class BaseGeometry:
    """Define class"""

    def area(self):
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
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
