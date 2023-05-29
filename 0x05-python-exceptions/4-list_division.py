#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for a in range(list_length):
        try:
            output = my_list_1[a] / my_list_2[a]
        except (ValueError, TypeError):
            print("wrong type")
            output = 0
        except ZeroDivisionError:
            print("division by 0")
            output = 0
        except IndexError:
            print("out of range")
            output = 0
        finally:
            newList.append(output)
    return newList
