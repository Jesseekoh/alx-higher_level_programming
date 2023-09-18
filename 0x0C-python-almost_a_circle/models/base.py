#!/usr/bin/python3
"""Base Class module"""


class Base:
    """Defines Base class
    """
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """Initialize Object

        Args:
            id (_type_, optional): _description_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
