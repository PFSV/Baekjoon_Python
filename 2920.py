# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:39:16 2022

@author: Doshite
"""
inp = list(map(int,input().split()))

if inp == sorted(inp):
    print("ascending")
elif inp == sorted(inp,reverse= True):
    print("descending")
else:
    print("mixed")