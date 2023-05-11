#!/usr/bin/python3

import sys

a = len(sys.argv) - 1

if a == 0:
    print("0 argument.")
elif a == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(a))
for i in range(a + 1):
    print("{}: {}".format(a,sys. argv[i]))
