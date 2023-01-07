#!/usr/bin/python3
"""square construction module"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """ Instantiation method
            Args:
                size (int): private instance attribute with default value 0
        """
        self.size = size

    @property
    def size(self):
        """ Property def size(self): to retrieve size

            Property setter def size(self, value) to set size as value
            Raises:
                TypeError: if size is not an integer
                ValueError: if size is < 0
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
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
