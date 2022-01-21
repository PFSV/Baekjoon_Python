# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 15:02:26 2022

@author: Doshite
"""

m = int(input())

cup = [1,2,3]

cup.append(4)



for i in range(m):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    cup[-1] = cup[a]
    cup[a] = cup[b]
    cup[b] = cup[-1]

cup.pop()

print(cup.index(1)+1)