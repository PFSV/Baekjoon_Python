# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 13:06:58 2022

@author: Doshite
"""
"""
시 분 초
초에 입력 받은 뒤, 초가 60 이상일 시, 초 = 초%60, 분 += 초//60
분 역시 마찬가지

시 : 시가 24 초과시, 시는 24의 나머지로 설정
"""
#시,분,초를 정수로 할당
hr,minn,sec = map(int,input().split())
sec += int(input())

if sec >= 60:
    minn += sec // 60
    sec = sec % 60

else:
    pass
if minn >= 60:
    hr += minn // 60
    minn = minn % 60

else:
    pass
if hr >= 24:
    hr = hr % 24
else:
    pass

print(hr,minn,sec)