t = int(input())
while t!=0:
    n=int(input())
    a=[int(x) for x in input().split()]
    a.sort()
    A=0
    B=0
    C=0
    D=0
    index = n//4
    x=index
    y=2*index
    z=3*index
    for i in range(n):
        if a[i]<a[x]:
            D=D+1
        elif a[i]>=a[x] and a[i] < a[y]:
            C=C+1
        elif a[i] >= a[y] and a[i] < a[z]:
            B=B+1
        elif a[i]>=a[z]:
            A=A+1
    if A==index and B==index and C==index and D==index:
        print(a[x],a[y],a[z])
        
    else:
        print("-1")
        
    t=t-1