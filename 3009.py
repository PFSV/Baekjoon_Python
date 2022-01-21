# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 14:21:07 2022

@author: Doshite
"""

dicx = {}
dicy = {}

for i in range(3):
    x,y = map(int,input().split())
    if x not in dicx:
        dicx[x] = 1
    else:
        dicx[x] += 1
    if y not in dicy:
        dicy[y] = 1
    else:
        dicy[y] +=1
    
r_dicx = dict(map(reversed,dicx.items()))
r_dicy = dict(map(reversed,dicy.items()))

print(r_dicx[1],r_dicy[1])

