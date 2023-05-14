#!/usr/bin/python3

def no_c(my_string):
    tempStr = my_string.translate({ord('c'): None})
    tempStr = tempStr.translate({ord('C'): None})
    return tempStr
