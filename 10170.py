#10170
"""a = NFC West       W   L  T
-----------------------
Seattle        13  3  0
San Francisco  12  4  0
Arizona        10  6  0
St. Louis      7   9  0

NFC North      W   L  T
-----------------------
Green Bay      8   7  1
Chicago        8   8  0
Detroit        7   9  0
Minnesota      5  10  1
"""
#print(a)


print((9*52)/((16**2+81)**(1/2)))

import math
import sys

d,h,w = map(int, sys.stdin.readline().split())

# h**2 + w**2 = d_ratio**2
# d_ratio = (h**2 + w**2)**(1/2)
# d_ratio * k = d, k = 실제 값으로 곱해지는 변수
# k = d / d_ratio
# k * h = 실제 높이
# k * w = 실제 너비

h_real = math.floor(h * (d / (h**2 + w**2)**(1/2)) )
w_real = math.floor(w * (d / (h**2 + w**2)**(1/2)))

print(h_real,w_real)