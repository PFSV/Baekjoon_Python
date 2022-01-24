# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 01:58:08 2022

@author: Doshite368
"""

s,k,h = map(int,input().split())

if s+k+h>=100:
    print("OK")
else:
    if s < k and s < h:
        print("Soongsil")
    elif k < s and k < h:
        print("Korea")
    elif h < s and h < k:
        print("Hanyang")