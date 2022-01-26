# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 22:24:55 2022

@author: Doshite368
"""

n = int(input())

for i in range(n):
    x,y = map(int,input().split())
    if x>=y:
        print("MMM BRAINS")
    else:
        print("NO BRAINS")