# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 14:39:14 2022

@author: Doshite
"""
#a 고정비용
#b 가변비용
# a+bn 생산비용 (n = bep)
# cn 총수입

'''
a+bn > cn
a > cn - bn
a > n(c-b)
a/(c-b) > n

'''

a,b,c = map(int,input().split())

if b>=c:
    print(-1)
else:
    print(int(a/(c-b)+1))