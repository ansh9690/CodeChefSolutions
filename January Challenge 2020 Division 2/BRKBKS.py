t=int(input())
while t!=0:
    s,w1,w2,w3=map(int , input().split())
    
    if w1+w2+w3<=s:
        print("1")
    elif w1+w2<=s or w2+w3<=s:
        print("2")
    else:
        print("3")
            
    t=t-1