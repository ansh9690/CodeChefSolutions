t = int(input())
while t!=0:
    s = input()
    count1=0
    for i in range(len(s)-1):
        if s[i]=="x" and s[i+1]=="y":
            count1=count1+1
            i=i+2
        else:
            count1=count1
            i=i+1
    print(count1)
    t=t-1