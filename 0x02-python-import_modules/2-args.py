#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    length = len(argv) - 1
    if length == 0:
        print("{:d} arguments.".format(length))
    elif length == 1:
        print("{:d} argument:".format(length))
    else:
        print("{:d} arguments:".format(length))
    list_args = []
    for i in argv:
        list_args += [i]
    for j in range(1, len(list_args)):
        print("{}: {}".format(j, list_args[j]))
