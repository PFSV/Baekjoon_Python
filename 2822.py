# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 20:40:31 2022

@author: Doshite368
"""

#총 점수  = 상위 5개 합 = 총 - 하위 3개

# 어떤 문제번호가 최종 점수에 포함되는지

#점수 : 문제번호로 딕셔너리(점수 넣으면 번호 나오게)

dic = {}
llist = []
for i in range(8): #0~7
    s = int(input()) #s는 점수, 입력값
    dic[s] = i+1 #s값당 1~8 할당
    llist.append(s) # 비교 위해 list
    
llist_ = sorted(llist) #크기 순서로 sort

slist = llist_[3::] #0,1,2번째를 제외한 3,4,5,6,7,8을 점수 리스트

print(sum(slist)) #llist의 총합, 총점


pslist = [] #출력 위한 리스트

for i in slist:
    pslist.append(dic[i])

pslist.sort()

for i in pslist:
    print(i,end=" ")
    
    
    