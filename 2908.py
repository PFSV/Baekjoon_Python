# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 19:57:56 2022

@author: Doshite
"""
a,b = input().split()

a = int(a[::-1])

b = int(b[::-1])

print(max(a,b))