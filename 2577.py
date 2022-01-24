# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 20:01:11 2022

@author: Doshite
"""

a= int(input())
b= int(input())
c= int(input())

mul = list(str(a*b*c))

for i in range(10):
    print(mul.count(str(i)))

