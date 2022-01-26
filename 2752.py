# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 22:23:16 2022

@author: Doshite368
"""

llist = list(map(int,input().split()))

llist.sort()

for i in llist:
    print(i,end=" ")