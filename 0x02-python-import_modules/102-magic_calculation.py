#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        sumation = add(a, b)
        for i in range(4, 6):
            sumation = add(sumation, i)
        return (sumation)

    else:
        return(sub(a, b))
