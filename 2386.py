# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 15:55:42 2022

@author: Doshite
"""

while True:
    
    inp = input()
    
    if inp == "#":
        break
    
    inp = inp.lower()
    
    inp = inp.replace(" ","")
    
    cha = inp[0]
    
    llist = []
    for i in inp:
        llist.append(i)
    
    llist.pop(0)
    
    num = llist.count(cha)
    
    print("{0} {1}".format(cha,num))
    
'''
while True:
    inp = input()
    if inp == "#":
        break
    cha, sen = inp[0],inp[1:].lower()
    count = sen.count(cha)
    print(cha,count)
'''

