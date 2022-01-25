# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:44:34 2022

@author: Doshite
"""
n = int(input())

a = list(map(int,input().split()))

a.sort()
for i in a:
    print(i,end =" ")