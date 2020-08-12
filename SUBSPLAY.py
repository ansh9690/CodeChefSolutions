t=int(input())
while t!=0:
    n=int(input())
    #s=input()
    a=input()
    ans=0
    for i in range(n-1):
        b=0
        for j in range(i+1,n):
            if a[i]==a[j]:
                b=(n-j+i)
                ans=max(ans,b)
                break
                # print(n-j+i)
           
                    
    print(ans)
    # print(a)
    t=t-1
