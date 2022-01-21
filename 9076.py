# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 22:43:05 2022

@author: Doshite
"""

t = int(input())

for _ in range(t):
    k = input().split()
    s = []
    for i in k:
        i = int(i)
        s.append(i)
        
    maxx = max(s)
    minn = min(s)
    
    s.remove(maxx)
    s.remove(minn)
    
    maxxx = max(s)
    minnn = min(s)
    
    if int(maxxx) - int(minnn) >=4:
        print("KIN")
    else:
        print(sum(s))

