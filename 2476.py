# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 22:26:49 2022

@author: Doshite368
"""

per = int(input())

pay = []
for _ in range(per):
    a, b, c = map(int,input().split())
    
    if a == b == c:
        pay1 = 10000 + a*1000
        pay.append(pay1)
    elif a == b != c or a == c != b:
        pay2 = 1000 + a*100
        pay.append(pay2)
    elif a != b == c:
        pay3 = 1000 + b*100
        pay.append(pay3)
    elif a != b != c:
        k = []
        k.append(a)
        k.append(b)
        k.append(c)
        pay.append(max(k)*100)
    
print(max(pay))
    