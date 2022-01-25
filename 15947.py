# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 20:16:37 2022

@author: Doshite368
"""

n = int(input())

if n % 14 == 1:
    print("baby")
if n % 14 == 13:
    print("baby")
if n % 14 == 0:
    print("sukhwan")
if n % 14 == 2:
    print("sukhwan")
if n % 14 == 6:
    print("cute")
if n % 14 == 10:
    print("bed")
if n % 14 == 5:
    print("very")
if n % 14 == 9:
    print("in")
    
if n % 14 == 3:
    if n//14 >=3:
        a = (n//14)+2
        print("tu+ru*"+str(a))
    else:
        p = (n//14)+2
        print("tu"+"ru"*p) 
        
if n % 14 == 7:
    if n//14 >= 3:
        a = (n//14)+2
        print("tu+ru*"+str(a))
    else:
        p = (n//14)+2
        print("tu"+"ru"*p) 
        
if n % 14 == 11:
    if n//14 >= 3:
        a = (n//14)+2
        print("tu+ru*"+str(a))
    else:
        p = (n//14)+2
        print("tu"+"ru"*p) 
        
if n % 14 == 4:
    if n//14 >= 4:
        b = (n//14)+1
        print("tu+ru*"+str(b))
    else:
        q = (n//14)+1
        print("tu"+"ru"*q) 
        
if n % 14 == 8:
    if n//14 >= 4:
        b = (n//14)+1
        print("tu+ru*"+str(b))
    else:
        q = (n//14)+1
        print("tu"+"ru"*q) 
        
if n % 14 == 12:
    if n//14 >= 4:
        b = (n//14)+1
        print("tu+ru*"+str(b))
    else:
        q = (n//14)+1
        print("tu"+"ru"*q) 
        