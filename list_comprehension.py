# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:03:22 2022

@author: Doshite
"""

#list comprehension

#점심 메뉴 + 디저트 경우의 수
x = [(x,y) for x in ["인문관","교식","외식"] for y in ["와대","공차","편의점"] ] 
#for 내부에 있는 게 매개변수, for문 앞에 있는 건 매개변수의 식
#다중 for문 가능


#print(x)

[print("지금 {0}시야, 점심 먹자".format(t)) for t in range(0,25) if t >= 11 and t <= 14]
#한 줄에 처리 가능

[print("지금 {0}시야, 점심 먹자".format(t)) for t in range(0,25) if t >= 11 and t <= 15]
#다중 if 문 가능
#if 처리 시 쉼표 x 그냥 넣기, 조건에 따른 결과 수행시키기 불가
