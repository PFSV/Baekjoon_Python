# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 19:50:45 2022

@author: Doshite
"""
odd = []

for _ in range(7):
    i = int(input())
    if i % 2 == 1:
        odd.append(i)

if len(odd) == 0:
    print(-1)
else:
    print(sum(odd))
    print(min(odd))