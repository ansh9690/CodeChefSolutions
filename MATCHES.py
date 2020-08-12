def numbers(r):
    if r==0:
        return 6
    elif r==1:
        return 2
        
    elif r==2:
        return 5
        
    elif r==3:
        return 5
        
    elif r==4:
        return 4
    
    elif r==5:
        return 5
        
    elif r==6:
        return 6
        
    elif r==7:
        return 3
    
    elif r==8:
        return 7
    
    elif r==9:
        return 6
t=int(input())
while t!=0:    
    a,b = map(int, input().split())
    c=a+b
    m=0
    while (c!=0):
        r=c%10
        m=m+numbers(r)
        c=c//10
    print(m)
    t=t-1
        