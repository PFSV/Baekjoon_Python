'''
꼭짓점 - 모서리 + 면 = 2
면 = 2 - 꼭짓점 + 모서리
'''

import sys

time = int(sys.stdin.readline())

for _ in range(time):
    v, e = map(int,sys.stdin.readline().split())
    s = 2 - v + e
    print(s) 
