#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boo=[]
    for i in range(len(my_list)-1):
        if my_list[i]%2==0:
            boo.append(1)
        else:
            boo.append(0)
    return boo
