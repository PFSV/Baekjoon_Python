# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:28:38 2022

@author: Doshite368
"""

t = int(input())

for i in range(t):
    n,d = map(int,input().split())
    nn = 0
    for i in range(n):
        v,f,c = map(int,input().split())
        if f>=c*d/v:
            nn+=1
    print(nn)