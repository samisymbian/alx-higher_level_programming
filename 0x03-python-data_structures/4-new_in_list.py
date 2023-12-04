#!/usr/bin/python3
def new_in_list(li,a,n):
    newl= li.copy()
    if a <0 or a > len(li)-1:
        return newl
    else:
        newl[a]=n
        return newl
