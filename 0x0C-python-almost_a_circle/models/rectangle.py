#!/usr/bin/python3
"""Rectangle Class module"""
from models.base import Base


class Rectangle(Base):
    """Defines Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        """Initializes object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width value

        Args:
            value (_type_): _description_
        """
        # validate value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height value

        Args:
            value (_type_): _description_
        """
        # validate value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x

        Args:
            value (_type_): _description_
        """
        # validate value
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y

        Args:
            value (_type_): _description_
        """
        # validate value
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the Area of Rectangle
        """

        return self.__width * self.__height

    def display(self):
        """prints out the rectangle instance to the
        stdout with #
        """
        print(end="\n" * self.y)
        for i in range(self.__height):
            print(' ' * self.x, end="")
            print('#' * self.__width)

    def __str__(self) -> str:
        """returns a strng representation of Rectangle class

        Returns:
            str: _description_
        """

        return '[Rectangle] ({}) {}/{} - {}/{}'\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns a value to each argument
        """

        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            # print("kwargs")
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
