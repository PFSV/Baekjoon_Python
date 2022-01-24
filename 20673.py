# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 00:37:59 2022

@author: Doshite
"""
# white, yellow, red

#white
# new case 50 per 1 million  & new hospitalization 10 per 1 million  at most

#red
# new hospitalization over 30 per 1 million

#yellow
#else

p = int(input()) #new case per 1 million
q = int(input()) #new hostilization per 1 million

if p <= 50 and q <= 10:
    print("White")
elif q > 30:
    print("Red")
else:
    print("Yellow")