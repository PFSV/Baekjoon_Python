dic = {}
llist = []

for i in range(5):
    a = list(map(int,input().split()))
    scr = sum(a)
    dic[scr] = i+1
    llist.append(scr)

print(dic[max(llist)],max(llist))    

