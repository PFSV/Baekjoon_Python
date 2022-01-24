# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 21:00:53 2022

@author: Doshite368
"""

n = input()

car = input().split()

cnt = 0

for i in car:
    if n == i:
       cnt +=1
print(cnt)