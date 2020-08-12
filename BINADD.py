# def add(a,b):
#     while b>0:
#         u=a^b    #decimal value
#         v=a&b
#         a=u
#         b=v*2
#     return a,b
        

t=int(input())
for i in range(t):
    x=input() 
    y=input() 
    
    a=int(x,2)    #decimal value
    b=int(y,2)    #decimal value
    c=0
    while b>0:
        u=a^b
        v=a&b
        a=u
        b=v*2
        c=c+1
    print(c)
    
    
    
    # print(a)
    # print(b)
    # print(a^b)
    # print(a&b)
    # print(add(22,16))
    