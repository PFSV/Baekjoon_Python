# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 13:29:21 2022

@author: Doshite
"""
ax,ay,az = map(int,input().split())

cx,cy,cz = map(int,input().split())

print(cx-az,int(cy/ay),cz-ax)

