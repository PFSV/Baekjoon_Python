# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 16:01:00 2022

@author: Doshite368
"""

p = int(input())

if p ==1:
    n = 1
else:
    n = 2
    while 3*n*(n-1)+2 <=p:
        n += 1
        
print(n)