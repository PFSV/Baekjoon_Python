# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 21:35:07 2022

@author: Doshite
"""
n = int(input())

for i in range(n):
    star = "*"*(i+1)
    print(star.center(n))