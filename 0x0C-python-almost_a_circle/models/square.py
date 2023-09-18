#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define Square class"""

    def __init__(self, size, x=0, y=0, id=None) -> None:
        """Initialize Square object

        Args:
            size (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """

        self.width = size
        self.height = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.height = value
        self.width = value
        self.__size = value

    def __str__(self) -> str:
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
