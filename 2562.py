# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 10:39:01 2022

@author: Doshite
"""
numlist = [int(input()) for _ in range(9)]

#반복 - 리터러블 당 반복 but 리터러블 == simple -> for 응용
# [] 바로 치기 -> array type 설정

maxval = numlist[0]

for i in numlist:
    if maxval <= i:
        maxval = i



print(maxval,(numlist.index(maxval)+1),sep ="\n")

#값 넣고, 위치(index) 반환 : list.index("값")