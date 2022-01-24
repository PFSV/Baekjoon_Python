# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 00:31:30 2022

@author: Doshite
"""

wc,hc,ws,hs = map(int,input().split())

if wc-ws >=2 and hc-hs >=2:
    print(1)
else:
    print(0)