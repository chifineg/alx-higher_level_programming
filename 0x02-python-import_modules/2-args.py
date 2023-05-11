#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv)
    print("{} arguments:".format(length - 1), end="")
    if length == 1:
        print(".")
    else:
        print(":")
    for i in range(1, length):
        print("{}: {}".format(i, sys.argv[i]))
