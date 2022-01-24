# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 01:29:31 2022

@author: Doshite
"""
while True:
    a,b,c = map(int,input().split())
    if a == b == c == 0:
        break
    llist = []
    llist.append(a)
    llist.append(b)
    llist.append(c)
    llist.sort()
    vid = max(llist)**2
    #print(vid)
    cal = 0
    for i in llist[0:2]:
        cal += i**2
        #print(cal)
    if vid == cal:
        print("right")
    else:
        print("wrong")
        