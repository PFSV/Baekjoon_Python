# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:37:41 2022

@author: Doshite
"""
l = int(input())
inp = input()
llist = []
s = 0
for i in inp:
    num = ord(i)-96
    num = num*(31**s)
    s += 1
    llist.append(num)
print(sum(llist) % 1234567891)

