#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv) - 1
    if length == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(length), end="")
    for i in range(length):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
