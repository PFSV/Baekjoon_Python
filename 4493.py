# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 14:48:42 2022

@author: Doshite
"""

"""
R P
P S
S R




"""


t = int(input())

for i in range(t):
    n = int(input())
    p1 = 0
    p2 = 0
    for i in range(n):
        i1,i2 = input().split()
        if i1 == "R" and i2 == "P":
            p2 += 1
        if i1 == "P" and i2 == "S":
            p2 += 1
        if i1 == "S" and i2 == "R":
            p2 += 1
        if i1 == "P" and i2 == "R":
            p1 += 1
        if i1 == "S" and i2 == "P":
            p1 += 1
        if i1 == "R" and i2 == "S":
            p1 += 1
    if p1 > p2:
        print("Player 1")
    if p1 == p2:
        print("TIE")
    if p1 < p2:
        print("Player 2")

