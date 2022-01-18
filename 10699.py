# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 21:25:15 2022

@author: Doshite368
"""

#오늘 날짜 가져오기

from datetime import datetime

print(datetime.today().strftime("%Y-%m-%d"))
    
#시간 format은 s t r f t i m e ( " 이용 " )

#print("{0}-{1}-{2}".format(year,month,day))