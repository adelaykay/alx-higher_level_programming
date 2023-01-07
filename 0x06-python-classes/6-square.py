#!/usr/bin/python3
"""square construction module"""


class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """ Instantiation method
            Args:
                size (int): private instance attribute with default value 0
                position (tuple)((int), (int)): private instance attribute,
                                 must be a tuple of 2 positive integers
            Attributes:
                __size (int): size of the square
                __position (tuple)((int), (int)):
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Property def position(self) to retrieve position

            Property setter def position(self, value) to set position as value
            Args:
                Value (tuple): must be a tuple of two positive integers
            Raises:
                TypeError: if postion is not a tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and isinstance(value[0], int)\
                and isinstance(value[1], int) and len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Calculates the area of a square

            Returns: area of the square or 0 if __size=0
         """
        if self.__size == 0:
            return (0)
        else:
            return (self.__size ** 2)

    def my_print(self):
        """prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for h in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print("", end=" ")
                for k in range(self.__size):
                    print("#", end="")
                print()
