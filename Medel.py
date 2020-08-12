t = int(input())
while t!=0:
    n = int(input())
    c= [int(x) for x in input().split()]
    d= c.copy()
    c.sort()
    for i in range(n):
        if c[0]==d[i] or c[-1]==d[i]:
            print(d[i] , end=' ')
    t=t-1