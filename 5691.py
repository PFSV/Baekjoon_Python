# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 15:10:45 2022

@author: Doshite
"""
while True:
    a, b = map(int,(input().split()))
    if a == 0 and b == 0:
        break
    else:
        print(a-(b-a))
    
    