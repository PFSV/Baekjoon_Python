# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 23:11:04 2022

@author: Doshite368
"""

n = int(input())

rmn = 0

for i in range(n):
    b,a = map(int,input().split())
    rmn += a%b

print(rmn)