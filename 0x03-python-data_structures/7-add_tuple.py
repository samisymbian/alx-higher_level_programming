#!/usr/bin/python3
def add_tuple(t1=(),t2=()):
    newt = ()
    ta=t1+(0,0)
    tb=t2+(0,0)
    newt=ta[0] + tb[0], ta[1] + tb[1]
    return newt
