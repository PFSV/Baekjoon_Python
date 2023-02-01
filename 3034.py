import sys

n,w,h = map(int, sys.stdin.readline().split())

d = (w**2 + h**2)**(1/2)

for i in range(n):
    m = int(sys.stdin.readline())
    if m <= d:
        print("DA")
    else:
        print("NE")