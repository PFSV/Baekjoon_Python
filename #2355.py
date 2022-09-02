import sys

for i in range(3):
    rot = int(sys.stdin.readline())
    ssum = 0
    for i in range(rot):
        num = int(sys.stdin.readline())
        ssum += num
    if ssum == 0:
        print(0)
    elif ssum > 0:
        print("+")
    else:
        print("-")