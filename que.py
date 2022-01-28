# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 14:43:42 2022

@author: Doshite
"""
#queue
"""
FIFO(first in first out)
데이터를 추가한 순서대로 제거 가능
파이썬에서 구현: list 활용
"""

#넣기, 빼기

queue = [1,2,3,4]

queue.append(5) #result: [1, 2, 3, 4, 5]
#append(x) : x의 요소를 array 맨 끝의 객체로 추가한다.
#x가 iterable하더라도 객체로 저장한다

queue.pop(0)
#iterable.pop(x) : iterable한 자료의 x인덱스의 요소를 반환해주고(변수로 설정하면 담을 수 있고,) 그 요소는 삭제한다.
#pop(0)은 첫 번째 요소를 제거함



