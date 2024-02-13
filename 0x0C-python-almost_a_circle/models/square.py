#!/usr/bin/python3
"""
    class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square is a special Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes an object instance"""
        self.size = size
        super().__init__(size, size, x, y)

    @property
    def size(self):
        """Attribute getter"""
        return self.width

    @size.setter
    def size(self, value):
        """"Attribute setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Custom string representation.

        Returns:
            str: A formatted string representing the object instance.
        """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id,
                        self.__x, self.__y, self.__width))

    def update(self, *args, **kwargs):
        """Updates the attributes.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        attributes = ['id', 'size', 'x', 'y']
        if args and len(args) > 0:
            self.__dict__.update(dict(zip(attributes, args)))
        elif kwargs:
            self.__dict__.update({k: v for k, v in kwargs.items()
                                 if k in self.__dict__})

    def to_dictionary(self):
        """Returns the dictionary representation"""
        print(self.__dict__)
