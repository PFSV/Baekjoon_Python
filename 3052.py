


list = [input() for _ in range(10)]

remainder = []

for i in list:
    rmn = int(i)%42
    remainder.append(rmn)

remainder = set(remainder)

setnum = 0
for _ in remainder:
    setnum +=1

print(setnum)


