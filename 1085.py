# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 13:32:59 2022

@author: Doshite
"""
x,y,w,h = map(int,input().split())

dx = 0
dy = 0
d = 0
if x >= w/2:
    dx += w-x
    if y>= h/2:
        dy += h-y
    else:
        dy += y
    if dx>=dy:
        d=dy
    else:
        d=dx
else:
    dx += x
    if y>= h/2:
        dy += h-y
    else:
        dy += y
    if dx>=dy:
        d=dy
    else:
        d=dx
        
print(d)