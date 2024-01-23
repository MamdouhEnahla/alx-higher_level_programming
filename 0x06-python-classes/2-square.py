#!/usr/bin/python3
"""Square"""


class Square:
    """Square"""

    def __init__(self, size=0):
        try:
            self.__size = size
        except TypeError as te:
            raise te("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
