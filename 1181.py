# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:54:43 2022

@author: Doshite
"""
llist = []

for _ in range(int(input())):
    word = input()
    llist.append(word)

llist = set(llist)    
llist = list(llist)

llist.sort()
llist.sort(key = len)


for i in llist:
    print(i)