#!/usr/bin/python3

"""
    module starts here
    this program draws a square
"""

def print_square(size):
    """ function starts here """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for x in range(size):
            print("#", end="")
        print()
