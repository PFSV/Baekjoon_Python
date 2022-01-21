# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 12:34:37 2022

@author: Doshite
"""
t = int(input())

n = int(input())

dic = {}

for i in range(n):
    a,b = input().split()
    b = int(b)
    dic[b] = a
    sdic = sorted(dic.items())

for _ in range(t):
    print(sdic[-1][-1])