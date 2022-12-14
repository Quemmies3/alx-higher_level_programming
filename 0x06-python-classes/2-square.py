#!/usr/bin/python3
"A Square Module."


class Square:
    """Construct of a square."""

    def __init__(self, size=0):
        """Constructor.
        Args:
            Size: The length of the sides of the square.
        Raise:
            TypeError: The arguement passed is not an integer.
            ValueError: The argument paseesd is less than zeror (0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
