#!/usr/bin/python3
"""square construction module"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """ Instantiation method
            Args:
                size (int): private instance attribute with default value 0

            Raises:
                TypeError: if size is not an integer
                ValueError: if size is < 0
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Calculates the area of a square

            Returns: area of the square or 0 if __size=0
         """
        if self.__size == 0:
            return (0)
        else:
            return (self.__size ** 2)
