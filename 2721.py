for _ in range(int(input())):
    n = int(input())
    w = sum((k*sum(range(k+2))) for k in range(1,n+1))
    print(int(w))
  
"""    
for _ in range(int(input())):
    n = int(input())
    for k in range(1,n+1):
        w = sum(k*sum(range(k+2)))
        print(w)
"""

#  int object is not iterable

'''
list comprehensioin required
'''