# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 23:56:05 2022

@author: Doshite368
"""



n = int(input())

llist = list(map(int,input().split()))
m = max(llist)
newlist = []
for i in llist:
    newlist.append(i/m*100)

print((sum(newlist)/len(newlist)))
    