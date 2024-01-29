#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """Representation of a Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for the private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """printable string representation of the rectangle"""
        string = ""
        if self.__width and self.__height:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """string representation of the rectangle for production"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message for deletion of a rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
