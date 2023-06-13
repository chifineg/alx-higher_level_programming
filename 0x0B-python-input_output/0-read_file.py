#!/usr/bin/python3
""" program starts here """


def read_file(filename=""):
    """function to read from a file """
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
