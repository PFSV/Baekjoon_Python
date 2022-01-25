# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 14:00:24 2022

@author: Doshite
"""

#[시작:얘의 앞까지:간격]


ssum = 0
n = int(input())
llist= list(map(int,input().split()))
#print(llist)
llist.sort()
#print(llist)
i = 1
for _ in llist:
    ssum += sum(llist[0:i])
    i +=1
print(ssum)