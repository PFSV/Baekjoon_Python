# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 23:22:26 2022

@author: Doshite368
"""

t = int(input())

for _ in range(t):
    s = int(input())
    n = int(input())
    op = 0
    for _ in range(n):
        q,p = map(int,input().split())
        op += q*p
    print(s + op)