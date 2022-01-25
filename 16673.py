# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 20:09:02 2022

@author: Doshite368
"""

summ = 0

c,k,p = map(int,input().split())

for i in range(c):
    summ += k*(i+1)+p*(i+1)**2

print(summ)