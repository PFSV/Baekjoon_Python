"""
a 300
b 60
c 10
"""

an = 0
bn = 0
cn = 0

t = int(input())

while t>=300:
    t -= 300
    an += 1
while t>=60:
    t -= 60
    bn += 1
    
if t % 10 == 0:
    cn = t//10
    print(an,bn,cn)
else:
    print(-1)
    

