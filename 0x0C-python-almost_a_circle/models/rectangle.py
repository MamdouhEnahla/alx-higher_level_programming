#!/usr/bin/python3
"""
    A class Rectangle that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle with width, height, position (x, y),
    and an optional identifier.

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes an object instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): the top-left corner (default is 0).
            y (int, optional): the top-left corner (default is 0).
            id (int, optional): An optional identifier. If provided,
            assigns it to the id attribute.Otherwise,
            inherits from the Base class constructor.
        """
        super().__init__(id)  # Call the superclass constructor
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the private attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the private attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the private attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the private attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the private attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the private attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the private attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the object instance"""
        return self.__width * self.__height

    def display(self):
        """prints the object instance to stdout"""
        print("\n" * self.__y, end="")
        side = " " * self.__x + "#" * self.__width
        print(side * self.__height)

    def __str__(self):
        """
        Custom string representation.

        Returns:
            str: A formatted string representing the object instance.
        """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.__x, self.__y, self.__width))

    def update(self, *args, **kwargs):
        """Updates the attributes.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) > 0:
            self.__dict__.update(dict(zip(attributes, args)))
        elif kwargs:
            self.__dict__.update({k: v for k, v in kwargs.items()
                                 if k in self.__dict__})

    def to_dictionary(self):
        """Returns the dictionary representation"""
        print(self.__dict__)
