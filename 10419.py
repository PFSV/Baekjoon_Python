# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 20:00:52 2022

@author: Doshite368
"""

for i in range(int(input())):
    d = int(input())
    t = 1
    while True:
        if d < t**2 + t:
            break
        else:
            t += 1
    t -= 1
    if d == 1:
        t = 0
    print(t)