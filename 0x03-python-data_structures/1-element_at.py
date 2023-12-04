#!/usr/bin/python3
def element_at(li, a):
    if a < 0 or a > len(li)-1:
        return 'None'
    else:
        return li[a]
