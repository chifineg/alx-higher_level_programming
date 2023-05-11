#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv)
    print("{} arguments:".format(length))
    if length == 1:
        print("1 argument:")
    elif length == 0:
        print("0 arguments")
    for i in range(length):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
