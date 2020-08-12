t=int(input())
while t!=0:
    n,m = map(int, input().split())
    b = [] 
    for i in range(n):	
    	a =[int(x) for x in input().split()] 
    	b.append(a) 
    count=n*m
    
    for i in range(1,n-1):
        for j in range(1,m-1):
            x=i-1
            y=i+1
            u=j-1
            v=j+1
            while (x!=-1 and y!=n) and (u!=-1 and v!=m):
                if b[i][u]==b[i][v] and b[x][j]==b[y][j]:
                    count+=1
                else:
                    break
                x=x-1
                y=y+1
                u=u-1
                v=v+1
    print(count)
    t=t-1