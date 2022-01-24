# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 22:03:02 2022

@author: Doshite368
"""
dic = {}

n = int(input())

for i in range(n):
    p = int(input())
    llist = []
    for i in range(p):
        pr,pln = input().split()
        pr = int(pr)
        dic[pr] = pln
        llist.append(pr)
    print(dic[max(llist)])
    