#!/usr/bin/python3

import re

def is_number(num):
    try:
        float(num)
        return True 
    except ValueError: 
        return False
def result2():
    list1 = input("1st list : ")
    list2 = input("2nd list : ")
    list11 =[]
    list22 =[]
    for N in range(len(list1)):
        if is_number(list1[N]) == True:
            list11.extend(list1[N])
    for N in range(len(list2)):
        if is_number(list2[N]) == True:
            list22.extend(list2[N])
    s1 = set(list11)
    s2 = set(list22)
    result1 = list(map(int, sorted(list(s1 | s2))))
    result2 = list(map(int, sorted(list(s1 & s2))))
    print("=> union ", result1)
    print("=> intersection ", result2)



