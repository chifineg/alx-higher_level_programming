#!/usr/bin/python3
""" program interpreter """


def append_write(filename="", text=""):
    """ function to append texts to a file

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.
    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        append_data = f.write(text)
        return append_data
