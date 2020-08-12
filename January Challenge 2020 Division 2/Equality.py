n,q=map(int, input().split())
arr = [int(g) for g in input().split()] 
li=[]
for f in range(n-1):
    if arr[f+1]-arr[f]>0:
        li.append(1)
    else:
        li.append(-1)
    
for i in range(q):
    l,r=map(int, input().split())
    if li[l-1]==li[r-2]:
        print("NO")
    else:
        print("YES")

