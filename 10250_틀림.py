# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 12:02:58 2022

@author: Doshite
"""
for i in range(int(input())):
    h,w,n = map(int,input().split())
    x = (n//h)+1
    y = n%h
    if y == 0:
        y = h
    room = y*100 + x
    print(room)