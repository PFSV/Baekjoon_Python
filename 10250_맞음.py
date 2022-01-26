for i in range(int(input())):
    h,w,n = map(int,input().split())
    if n % h != 0:
        y = n % h
        x = n//h +1
    else:
        y = h
        x = n//h
    room = y*100 + x
    print(room)
    
    #경계에 집중, 미리 나누기