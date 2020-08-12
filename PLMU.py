t = int(input())
while t!=0:
    n=int(input())
    a=[int(i) for i in input().split()]
    # print(a)
    count=0
    c=0
    for i in range(n):
        if a[i]==2:
            count=count+1
    for j in range(n):
        if a[j]==0:
            c=c+1
    # print(count)
    # print(c)
    x=(count*(count-1))//2
    y=(c*(c-1))//2
    print(x+y)
    
    t=t-1