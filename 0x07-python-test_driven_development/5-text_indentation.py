#!/usr/bin/python3

"""
    module starts here
    program to indent given texts
"""

def text_indentation(text):
    """ function starts here """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
