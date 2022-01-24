# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 00:34:36 2022

@author: Doshite
"""
a = list(map(int,input().split()))

ssum = 0

for i in a:
    i = int(i)
    ssum += 5*i

print(ssum)