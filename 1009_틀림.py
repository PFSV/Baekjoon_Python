
for _ in range(int(input())):
    a,b = map(int,input().split())
    result = (a**b)%10
    if result == 0:
        result = 10
    print(result)
        
        
#자리수 = 10*n의자리로 나눈 나머지 ex. k의 1의자리수 = k%10
#모르겠어