# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 16:44:29 2022

@author: Doshite
"""

c = 100
s = 100

r = int(input())

for i in range(r):
    a,b = map(int,input().split())
    if a>b:
        s -= a
    elif a<b:
        c -= b
    else:
        pass
    

print(c)
print(s)