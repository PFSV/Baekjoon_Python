# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 22:23:11 2022

@author: Doshite368
"""

# 나이가 많으려면
'''
1. year 작음
2. month 큼큼
3. date 큼
'''

dic = {}
llist = []
n = int(input())

for i in range(n):
    a,b,c,d = input().split()
    b = int(b)
    c = int(c)
    d = int(d)
    cal = b+ 10*c+ 100*d
    llist.append(cal)
    dic[cal] = a
    
print(dic[max(llist)])
print(dic[min(llist)])

    


