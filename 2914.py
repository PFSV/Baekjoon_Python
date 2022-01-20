v = int(input())

inp = input()

ab = []
for i in inp:
    ab.append(i)


a = ab.count("A")
b = ab.count("B")


if a>b:
    print("A")
elif a<b:
    print("B")
else:
    print("Tie")
