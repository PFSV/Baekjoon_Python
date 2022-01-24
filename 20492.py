# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 00:46:52 2022

@author: Doshite
"""
n= int(input())

#1
a = n*(78/100)

#2
kyung = n *(80/100)

tax_sub = n *(20/100)*(78/100)


b = kyung + tax_sub

print(int(a),int(b))