#!/usr/bin/python3
"""Square construction module"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """ Args:
                size (int): private instance attribute with default value 0

            Raises:
                TypeError: if size is not an integer
                ValueError: if size < 0
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
