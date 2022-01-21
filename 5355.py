t = int(input())

for i in range(t):
    inp = input().split()
    
    summ = float(inp[0])
    
    for i in inp[1::]:
        if i == "@":
            summ *=3
        if i == "%":
            summ +=5
        if i == "#":
            summ -=7
    print("{:.2f}".format(summ))

