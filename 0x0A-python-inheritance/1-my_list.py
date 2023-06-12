#!/usr/bin/python3
"""
program starts here
"""


class MyList(list):
    """list is supperclass of MyList"""
    def print_sorted(self):
    """Object initialization
    Prints a sorted list in ascending order
    """

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))

