# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 14:50:39 2022

@author: Doshite
"""
#알파벳 불러오기

import string

alpha = string.ascii_lowercase


char = input()

dic = {}

for i in alpha:
    if i in char:
        dic[i] = char.index(i)
    else:
        dic[i] = -1

for i in dic.values():
    print(i, end= " ")
