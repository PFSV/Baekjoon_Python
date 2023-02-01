import sys

for _ in range(int(sys.stdin.readline())):
    a = list(map(int,sys.stdin.readline().split()))
    ssum = 0
    b = []
    for i in a:
        if i % 2 == 0:
            ssum += i
            b.append(i)
    print(ssum,min(b))
            