# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 13:59:59 2022

@author: Doshite
"""
h, m = map(int,input().split())
t = int(input())
m += t

if m>=60:
    h += m//60
    m = m%60

if h >=24:
    h -= 24
    
print(h,m)