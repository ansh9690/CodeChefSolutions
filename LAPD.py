t=int(input())

while t>0:
    count=0
    A,B,C = map(int, input().split())
    for i in range(2,A+1):
        for j in range(1,B+1):
            for k in range(1,C+1):
                if (j*j)-(i-1)*(k-1) < 0:
                    count+=1
    t=t-1                              
    print(count)                