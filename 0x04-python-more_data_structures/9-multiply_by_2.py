#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    "mutiply value by 2"
    newd = {}
    for key, value in a_dictionary.items():
        newd.update({key: (value * 2)})
    return newd
