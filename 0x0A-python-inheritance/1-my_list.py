#!/usr/bin/python3
"""
program starts here
"""


class MyList(list):
    """list is supperclass of MyList"""
    def __init__(self):
        """object initialization"""
        super().__init__()

    def print_sorted(self):
        """sorts list in ascending order"""
        print(sorted(self))
