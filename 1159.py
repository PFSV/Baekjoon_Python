# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 19:16:00 2022

@author: Doshite
"""
nlist = []
result = []
for i in range(int(input())):
    name = input()[0]
    nlist.append(name)
    
for i in set(nlist):
    time = nlist.count(i)
    if time >= 5:
        result.append(i)

result.sort()

if len(result) == 0: #내부 원소 개수 = len 
    print("PREDAJA")
else:
    for i in result:
        print(i,end="")