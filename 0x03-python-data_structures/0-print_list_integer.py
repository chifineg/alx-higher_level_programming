#!/usr/bin/python3

def print_list_integer(my_list=[]):
    length = len(my_list)
    for i in range(length):
        print("{:s}".format(my_list[i]))

print_list_integer()
