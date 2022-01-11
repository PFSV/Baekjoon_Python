# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 21:46:13 2022

@author: Doshite
"""

n,x= map(int,input().split())
seq = list(map(int,input().split()))

result = []

for i in seq:
    if i < x:
        result.append(i)
    else:
        pass

for i in result:
    print(i,end=" ")
    