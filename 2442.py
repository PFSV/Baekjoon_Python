# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 23:13:28 2022

@author: Doshite368
"""

n = int(input())

for p in range(n):
    i = p +1
    k = "*"*(2*i-1)

    print(k.center(2*n-1))
    
    
    # 나머지를 공백으로 채워서 에러, 앞에것만 공백 채우게
    
N = int(input())

for i in range(1,N+1):

    b = ' '*(N-i)+'*'*((2*i)-1)

    print(b)