# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 19:41:48 2022

@author: Doshite
"""
ppl = []
per = 0

for _ in range(10):
    o,i = map(int,input().split())
    per -= o
    per += i
    ppl.append(per)

print(max(ppl))