#!/usr/bin/python3
def uniq_add(my_list=[]):
    "adds unique number"
    total = 0
    newl = []
    for element in my_list:
        if element not in newl:
            total+= element
            newl.append(element)
    return total
