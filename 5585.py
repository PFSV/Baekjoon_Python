# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 16:17:07 2022

@author: Doshite
"""


n = int(input())
m = 1000 - n
#print("m",m)
n500 = 0
n100 = 0
n50 = 0
n10 = 0
n5 = 0
n1 = 0

while m >= 500:
    m-=500
    n500+=1
#print("500",n500)
while m >= 100:
    m -= 100
    n100 += 1
#print("100",n100)
while m >= 50:
    m -= 50
    n50 += 1
#print("50",n50)
while m >= 10:
    m -= 10
    n10 += 1
#print("10",n10)
while m>=5:
    m -= 5
    n5 += 1
#print("5",n5)
while m >=1:
    m -= 1
    n1 += 1
#print("1",n1)


print(n500+n100+n50+n10+n5+n1)



        