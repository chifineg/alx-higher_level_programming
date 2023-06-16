#!/usr/bin/python3
""" program interpreter starts here """
from models.base import Base


class Rectangle(Base):
    """ Rectangle subclass that inherits from Base class

    private attribute:
        __width
        __height
        __x
        __y
    """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """ function to return the width and height
            of a rectangle

        Args:
            width
            height
            x
            y
            id
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

        def getWidth(self):
            return self.__width
        def getHeight(self):
            return self.__height
        def getX(self):
            return self.__x
        def getY(self):
            return self.__y
