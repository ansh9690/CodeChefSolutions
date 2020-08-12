# import operator as op
# from functools import reduce

# def nCr(n, r):
#     r = min(r, n-r)
#     numer = reduce(op.mul, range(n, n-r, -1), 1)
#     denom = reduce(op.mul, range(1, r+1), 1)
#     return numer // denom

# n,k=map(int , input().split())
# # n=int(input())
# a=[int(x) for x in input().split()]
# a.sort()
# # print(a)
# b=[]

# for i in range(n-1):
#     if a[i] !=a[i+1]:
#         b.append(a[i])

#     else:
#         continue

# b.append(a[-1])

# x=len(b)
# # print(x)
# s=0
# while k >= 0:
#     s = s+nCr(x,k)
#     k=k-1 
# print(s)

# #......

# import operator as op
# from functools import reduce

# def nCr(n, r):
#     r = min(r, n-r)
#     numer = reduce(op.mul, range(n, n-r, -1), 1)
#     denom = reduce(op.mul, range(1, r+1), 1)
#     return numer // denom


# n,k = map(int, input().split())

# a=[int(x) for x in input().split()]
# a.sort()

# x=len(a)
# # print(x)
# s=0
# while k >=0:
#     s = (s+nCr(x,k))%1000000007
#     k=k-1 
    
# print(s)

#include<bits/stdc++.h>
#define pb push_back

