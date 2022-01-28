# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 14:53:46 2022

@author: Doshite
"""
"""
입력값이 두 개 혹은 한 개이므로 리스트로 받고, 
llist[0]이 push일 때 llist[1]을 처리하도록 하자

llist = list(input().split())

push x 
append
"""

#요소가 한 개여도 split 문제없이 수행 

queue = []

for i in range(int(input())):
    llist = list(input().split())
    word = llist[0]

    #push    
    if word == "push":
        queue.append(llist[1])
    
    #pop
    if word == "pop":
        if queue == []:
            print(-1)
        else:
            print(queue.pop(0))
            
    #size
    if word == "size":
        print(len(queue))
    
    #empty
    if word == "empty":
        if queue == []:
            print(1)
        else:
            print(0)
            
    #front
    if word == "front":
        if queue == []:
            print(-1)
        else:
            print(queue[0])
            
    #back
    if word == "back":
        if queue == []:
            print(-1)
        else:
            print(queue[-1])
            
    
#시간 초과-> import() 대신 stdin 사용
# list = []도 있지만, len(queue) == 0도 가능
from sys import stdin

queue = []

N = int(stdin.readline())

for i in range(N):
    llist = stdin.readline().split()
    word = llist[0]

    #push    
    if word == "push":
        queue.append(llist[1])
    
    #pop
    if word == "pop":
        if queue == []: #if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
            
    
    #size
    if word == "size":
        print(len(queue))
    
    #empty
    if word == "empty":
        if queue == []:
            print(1)
        else:
            print(0)
            
    #front
    if word == "front":
        if queue == []:
            print(-1)
        else:
            print(queue[0])
            
    #back
    if word == "back":
        if queue == []:
            print(-1)
        else:
            print(queue[-1])
            











        