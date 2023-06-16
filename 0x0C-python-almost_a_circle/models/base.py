#!/usr/bin/python3
""" program interpreter starts here """


class Base:
    """ Base class starts here

    private attribute:
        __nb_objects
    """
    
    __nb_objects = 0
    def __init__(self, id=None):
        """ function to handle values for id

        Args:
            id
        """
        if id is not None:
            self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects
