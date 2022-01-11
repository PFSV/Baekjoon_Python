# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 21:57:12 2022

@author: Doshite
"""
t = int(input())

for i in range(t):
    a,b = map(int, input().split())
    print("Case #{0}: {1}".format(i+1,a+b))