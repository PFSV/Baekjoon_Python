n = int(input())
val = list(map(int,input().split()))
# map 함수 치면, 일렬로 할 것, 해당되는 것에 넣어지고, map 객체 반환

maxval = val[0]
minval = val[0]
for i in val:
    if maxval <= i:
        maxval = i
    if minval >= i:
        minval = i

print(minval,maxval,end = " ")


