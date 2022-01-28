# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 13:35:22 2022

@author: Doshite
"""
"""
Rev(): 리스트 역순으로 읽기 : list[::-1]
리스트->문자열->정수->연산->문자열->리스트

llist = [1,2,3,0]
llist = llist[::-1]
strr = ""
for i in llist:
    strr += str(i)

print(int(strr))
print(1+(int(strr)))
"""

x,y = input().split()

xlist = []
ylist = []

for i in x:
    xlist.append(i)
for i in y:
    ylist.append(i)

xlist = xlist[::-1]
ylist = ylist[::-1]

xstr = ""
ystr = ""

#list를 바로 str로 바꿀 수 있나? 
'''
llist = [a,b,c]
str = "".join(llist)
'''
'''
for i in xlist:
    xstr += str(i)
for i in ylist:
    ystr += str(i)
'''

xstr = "".join(xlist)
ystr = "".join(ylist)

ssum= int(xstr)+int(ystr)

slist = []
for i in str(ssum):
    slist.append(i)

slist = slist[::-1]

'''
sstr = ""
for i in slist:
    sstr += str(i)
'''

sstr = "".join(slist)

print(int(sstr))
