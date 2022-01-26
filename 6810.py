# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 22:15:46 2022

@author: Doshite368
"""

ssum = 9 * 1 + 7 * 3 + 8 * 1 + 0 * 3 + 9 * 1 + 2 * 3 + 1 * 1 + 4 * 3 + 1 * 1 + 8 * 3

a = int(input())
a = a*1
ssum +=a

b = int(input())
b = b*3
ssum += b

c = int(input())
c = c*1
ssum += c


print("The 1-3-sum is {0}".format(ssum))