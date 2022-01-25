# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:50:16 2022

@author: Doshite
"""

llist = list(map(int,input().split()))

#a b c

c = max(llist)
llist.remove(c)

b = max(llist)
llist.remove(b)

a = max(llist)

dic = {"A":a,"B":b,"C":c}

i = input()

for p in i:
    print(dic[p],end=" ")




 



