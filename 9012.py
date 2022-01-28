# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 14:34:58 2022

@author: Doshite
"""
"""
(의 개수와 )의 개수가 동일하면 yes

정수 받은 개수 만큼 input 받고, 문자열의 (와 )각각 count해서 비교
"""

for _ in range(int(input())):
    strr = input()
    left = strr.count("(")
    right = strr.count(")")
    if left == right:
        print("YES")
    else:
        print("NO")
        
#예제입력2-3에서 걸림, "(",")"의 순서 맞출 필요 있음

