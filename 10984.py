# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 23:01:48 2022

@author: Doshite368
"""

t = int(input())

for i in range(t):
    n = int(input())
    crd = 0 #들은 학점 수
    scr = 0 #받은 총점
    for i in range(n):
        a,b = map(float,input().split())
        crd += a
        scr += a*b
    print(int(crd),round(scr/crd,1))