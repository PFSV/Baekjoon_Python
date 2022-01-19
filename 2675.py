# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:09:19 2022

@author: Doshite
"""

#trial 1
'''
t = int(input())

r,s = input().split()

r = int(r)

for i in s:
    i = i*r
    print(i,end = "")
# 2번이상 반복해야함

t = int(input())

ex = [input() for _ in range(t)] #한 줄에 있을 값들이 리스트로 들어옴

for i in ex:
    r,s = i.split()
    r = int(r)
    for k in s:
        k = k*r
        print(k, end = "")
        
    
t = int(input())

for i in range(t):
    r, s = input().split()
    r = int(r)
    for i in s:
        i = i*r
    print(i)
'''
t = int(input())
for i in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)