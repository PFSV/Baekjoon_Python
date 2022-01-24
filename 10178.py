# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 23:20:03 2022

@author: Doshite368
"""



t = int(input())

for _ in range(t):
    c,v = map(int,input().split())
    y = c // v
    d = c%v
    print("You get {0} piece(s) and your dad gets {1} piece(s).".format(y,d))