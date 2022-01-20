'''
import math

word = input()
half = (len(word)/2)

if len(word) %2 == 1:
    half_down_index = math.floor(half) - 1
    reverselist = word[half_down_index:-1]
    reverselist = reversed(reverselist)
    
    if word[0:half_down_index] == reverselist:
        print(1)
    else:
        print(0)
    
else:
    reverselist_ = word[half:-1]
    reverselist_ = reversed(reverselist_)
    if word[0:half] == reverselist_:
        print(1)
    else:
        print(0)

word = input()

wordnum = len(word)

halfnum = round(wordnum / 2)

frontword = word[0:halfnum-1]

backword = word[halfnum::1]


reversedbackword = backword[::-1]


if reversedbackword == frontword:
    print(1)
else:
    print(0)
'''
word = list(str(input()))

if list(reversed(word)) == word:
    print(1)
else:
    print(0)
    
    #있는 그대로 생각하기
    