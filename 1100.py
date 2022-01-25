# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 13:53:58 2022

@author: Doshite
"""
wf = 0

for i in range(8):
    inp = input()
    k = i+1
    if k%2 ==1:
        wf += inp[::2].count("F")
    if k%2 == 0:
        wf += inp[1::2].count("F")

print(wf)
            