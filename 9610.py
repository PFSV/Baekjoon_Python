num = int(input())

q1 = 0
q2 = 0
q3 = 0
q4 = 0
q5 = 0

for i in range(num):
    x,y = map(int,input().split())
    
    if x>0 and y>0:
        q1 += 1
    if x<0 and y>0:
        q2 += 1
    if x<0 and y<0:
        q3 += 1
    if x>0 and y<0:
        q4 += 1
    if x==0 or y == 0:
        q5 += 1
    
print("Q1: {0}\nQ2: {1}\nQ3: {2}\nQ4: {3}\nAXIS: {4}".format(q1,q2,q3,q4,q5))