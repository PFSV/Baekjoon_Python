# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 01:59:06 2022

@author: Doshite
"""
s = int(input())

ee = 0
ie = 0

sen = input()
for i in sen:
    if i == "2":
        ie += 1
    if i == "e":
        ee += 1

if ie >ee:
    print("2")
elif ie<ee:
    print("e")
else:
    print("yee")
        