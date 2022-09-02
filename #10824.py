a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

x = a * p

if p <= c:
    y = b
else:
    y = b + (p - c)*d

if x >= y:
    print(y)
else:
    print(x)