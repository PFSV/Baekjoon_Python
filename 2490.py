# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 15:37:08 2022

@author: Doshite
"""

"""

배 = 0
등 = 1

*배(0)의 개수
도 = 1 = A
개 = 2 = B
걸 = 3 = C
윷 = 4 = D
모 = 0 = E
"""

b = 0

for i in range(3): 
    a = input().split(" ")
    for i in a:
        if i == "0":
            b += 1
    if b == 1:
        print("A")
    elif b == 2:
        print("B")
    elif b == 3:
        print("C")
    elif b == 4:
        print("D")
    elif b == 0:
        print("E")
    b = 0
    
