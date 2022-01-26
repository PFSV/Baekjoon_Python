# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 14:17:09 2022

@author: Doshite
"""
a,b,v = map(int,input().split())

'''
h = 0
day = 1
while True:
    h += a
    if h >= v:
        break
    else:
        h -= b
    day += 1

print(day)
    '''

if (v-b)%(a-b) == 0:
    day = (v-b)/(a-b)
else:
    day = (v-b)//(a-b) + 1

print(int(day))