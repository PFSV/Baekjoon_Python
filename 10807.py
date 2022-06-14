import sys
n = int(input())
numlist = sys.stdin.readline().split()
findnum = int(input())

num = 0


for i in numlist:
    if findnum == int(i):
        num += 1

print(num)