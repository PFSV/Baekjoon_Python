# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 01:06:18 2022

@author: Doshite
"""

s = int(input())
m = int(input())
l = int(input())

hcr = s + 2*m + 3*l

if hcr >= 10:
    print("happy")
else:
    print("sad")