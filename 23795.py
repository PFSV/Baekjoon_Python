# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 00:16:10 2022

@author: Doshite
"""
ssum = 0

while True: 
    m = int(input())
    if m == -1:
        break
    ssum += m
    
print(ssum)