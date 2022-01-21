# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 22:36:17 2022

@author: Doshite
"""
s = input()
for i in s:
    if i.islower():
        print(i.upper(),end="")
    elif i.isupper():
        print(i.lower(),end="")
    
