#!/usr/bin/python3
""" program interpreter """


def write_file(filename="", text=""):
    """ function to write texts to a file 
    
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        write_data = f.write(text)
        return write_data
