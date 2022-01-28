# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 15:25:51 2022

@author: Doshite
"""
"""
queue = []

( 이면 push
 ) 면 pop

전체 루틴 돌리고, queue 가 empty여야함, 그렇지 않으면 no
만약 empty인데 pop 뜨면, no
+ no를 출력시키면, no를 출력하고, word loop를 다 돌린 다음에,
다시 queue size로 yes,no판별 -> queue size로 yes no 통일시키되, no 출력시키기 위해
)가 들어오면 그걸 queue에 남겨 (size= 1)로 만듬.
"""


for i in range(int(input())):
    word = input()
    que = []
    for i in word:
        if i == "(":
            que.append(i)
        elif i == ")":
            if len(que) != 0:
                que.pop(0)
            else:
                que.append(i)
                break

    if len(que) == 0:
        print("YES")
    else:
        print("NO")