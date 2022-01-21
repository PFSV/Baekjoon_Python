# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 12:27:44 2022

@author: Doshite
"""
n = int(input())

cute = 0
ncute = 0

for _ in range(n):
    ans = int(input())
    if ans == 1:
        cute += 1
    else:
        ncute += 1
        
if cute>ncute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")