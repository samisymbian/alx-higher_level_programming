#!/usr/bin/python3
def replace_in_list(li,a,n):
    if a < 0 or a > len(li)-1:
        return li
    else:
        li[a]=n
        return li
