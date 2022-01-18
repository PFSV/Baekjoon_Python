# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 21:10:00 2022

@author: Doshite368
"""

t = int(input())
num = 0
for _ in range(t):
    a,b = map(int,input().split())
    c = a + b
    num += 1
    print("Case #{0}: {1} + {2} = {3}".format(num,a,b,c))