# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 21:51:33 2022

@author: Doshite368
"""

score = [input() for _ in range(5)]

summ = 0

for i in score:
    i = int(i)
    if i < 40:
        i = 40
        summ += i
    else:
        summ += i
        
print(int(summ/5))