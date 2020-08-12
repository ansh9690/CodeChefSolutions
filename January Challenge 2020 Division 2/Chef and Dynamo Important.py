import sys

T = int(input())

while(T!=0):
    n = int(input())
    a = int(input())
    s = a+2*(10**n)
    print(s)
    sys.stdout.flush()
    b = int(input())
    c = (10**n)-b
    print(c)
    sys.stdout.flush()
    d = int(input())
    e = (10**n)-d
    print(e)
    sys.stdout.flush()
    x = int(input())
    if x==-1:
        continue
    
    T-=1

 