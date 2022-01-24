# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 15:47:20 2022

@author: Doshite
"""

a = input().split()

summ = 0

for i in a:
    i = int(i)
    summ += i**2


print(summ%10)
    