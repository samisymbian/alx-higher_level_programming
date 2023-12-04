#!/usr/bin/python3
def print_reversed_list_integer(li):
    newl=[]
    rova=len(li)-1
    i = len(li)-1
    s=0
    while s <= i:
        newl.append(li[rova])
        rova= rova -1
        s= s +1
    for j in range(len(newl)):
        print("{:d}".format(newl[j]))
