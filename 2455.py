# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 21:19:04 2022

@author: Doshite368
"""

"""
32
42
39




"""


llist = []

num = 0

for _ in range(4):
    i,o = map(int,input().split())
    num -= i
    num += o
    llist.append(num)  #i,o 바뀜
    
llist.sort()



print(llist[-1])
