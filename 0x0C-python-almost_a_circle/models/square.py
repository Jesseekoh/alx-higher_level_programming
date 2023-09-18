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
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assign a value to each argument"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        square_dict = {}

        square_dict["id"] = self.id
        square_dict["width"] = self.width
        square_dict["height"] = self.height
        square_dict["x"] = self.x
        square_dict["y"] = self.y
        return (square_dict)

    def __str__(self) -> str:
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
