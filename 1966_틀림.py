# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 16:08:31 2022

@author: Doshite
"""
"""
중요도 체크 후 중요도가 list의 max값이 아닌 경우,

가장 뒤로 이동(앞에것 pop, 뒤로 append)

중요도가 같은 값이 있으면? 
>어쨌든 max 값에 해당하기만 하면 됨 > 딕셔너리(x가 많지,y는 안 중요)

중요도 체크 어떻게? 
>{문서 번호: 중요도}, 번호에 해당하는 value값, 
>value 리스트가 중요도 리스트

맨 왼쪽이 0!!
> 마지막 출력시 + 1, 그전까진 0부터 인덱스 세기
"""
'''
for _ in range(int(input())):
    que = []
    dic = {}
    vol, oord = map(int,input())
    value  = list(map,int(input().split()))
    for i in value:
        dic[value.index(i)] = value
        #value들의 que에서 순서를 넣으면, 그 순서에 해당하는 value값을 반환
        #근데 그냥 이게 이 큐(리스트)에서 max가 아니면, 그냥 뒤로 빼도 되지 않나?
        
   '''     
'''
프린트 했는지 여부로 출력순서 세기
해당 숫자 들어오면 출력순서에 +1하고 멈추기
        
'''
        
for _ in range(int(input())):
    vol,oord = map(int, input().split())
    que = list(map(int, input().split()))
    for i in que:
        print(i)
        prto = 0
        if i == oord:
            if i == max(que):
                prto += 1
                print(prto)
            else:
                que.pop(0)
                que.append(i)
        else:
            if i == max(que):
                prto +=1
                que.pop(0)
            else:
                print(i)
                que.pop(0)
                que.append(i)
    print(prto)
            
        
    
    
    
    
    
    
    
    
    