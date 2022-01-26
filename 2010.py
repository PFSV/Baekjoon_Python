import sys

com = 0
n = int(sys.stdin.readline())
for i in range(n):
    m = int(sys.stdin.readline())
    com += m

com -= (n-1)

print(com)
