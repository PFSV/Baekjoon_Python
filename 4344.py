# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 20:52:45 2022

@author: Doshite368
"""

for i in range(int(input())):
    llist = list(map(int,input().split()))
    num = llist[0]
    #print(num)
    llist.remove(num)
    #print(llist)
    summ = sum(llist)
    mean = summ/num
    #print(mean)
    over = 0
    for i in llist:
        if float(i) > mean:
            over +=1
    #print("over"+str(over))
    result = over/num*100
    print("{:.3f}%".format(result))
    #print(str(round(over/num, 3))+"%")