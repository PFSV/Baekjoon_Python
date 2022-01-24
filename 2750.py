# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 01:16:15 2022

@author: Doshite
"""
n = int(input())
llist = []
for i in range(n):
    a = int(input())
    llist.append(a)

llist.sort()

for i in llist:
    print(i)