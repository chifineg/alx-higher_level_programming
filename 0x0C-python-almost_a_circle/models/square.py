#!/usr/bin/python3
"""program interpreter"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """subclass square that inherits from class rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """square function

        args:
            size
            x
            y
            id
        """
        super().__init__(size, size, x, y, id)
