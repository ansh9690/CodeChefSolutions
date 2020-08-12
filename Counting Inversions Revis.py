t = int(input())
while t!=0:
    n,k = map(int, input().split())
    a = [int(x) for x in input().split()]
    inv=0
    for i in range(n):
        flag=0
        p1=0
        p2=0
        for j in range(n):
            if i==j:
                flag=flag+1
            elif a[i]>a[j] and flag==1:
                p2=p2+1
                
            elif a[i]>a[j] and flag==0:
                p1=p1+1
        count = p1+p2
        inv = inv+(count*(k*k+k)//2-p1*k)
    print(inv)
    t = t-1