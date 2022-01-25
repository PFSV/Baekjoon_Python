# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:14:52 2022

@author: Doshite368
"""

t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    print("Case {0}: {1}".format(i+1,a+b))