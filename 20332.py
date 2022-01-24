# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 00:54:42 2022

@author: Doshite
"""
n = int(input())

a = list(map(int,input().split()))

summ = 0

for i in a:
    summ += i

rmn = summ % 3

if rmn == 0:
    print("yes")
else:
    print("no")