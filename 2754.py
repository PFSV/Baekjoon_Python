# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 16:29:00 2022

@author: Doshite
"""
'''
dic = {}

dic["A+"] = 4.3
dic["A0"] = 4.0
dic["A-"] = 3.7

dic["B+"] = 3.3
dic["B0"] = 3.0
dic["B-"] = 2.7

dic["C+"] = 2.3
dic["C0"] = 2.0
dic["C-"] = 1.7

dic["D+"] = 1.3
dic["D0"] = 1.0
dic["D-"] = 0.7
dic["F"] = 0.0

score = input()

print(dic[score])
'''
#runtime error - > b/c "F":0.0 miscode

dic = {"A+": 4.3, "A0": 4.0, "A-": 3.7,"B+": 3.3, "B0": 3.0, "B-": 2.7,"C+": 2.3, "C0": 2.0, "C-": 1.7,"D+": 1.3, "D0": 1.0, "D-": 0.7,"F": 0.0}


print(dic[str(input())])