#!/usr/bin/python3
def search_replace(my_list, search, replace):
    "replaces an element with another"
    for i in range(len(my_list)-1):
        if my_list[i] == search:
            my_list[i] = replace
    return my_list
