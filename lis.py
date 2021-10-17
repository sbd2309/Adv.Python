import numpy as np
def _lis(l,n):
    global max

    if n==1:
        return 1
    else:
        for i in range(1,n):
            r=_lis(n,i)

def lis(l):
    global maxi
    n=len(l)

    maxi=1
    _lis(l,n)
    return maxi

n = int(input())
l = [int(i) for i in input().strip().split(' ')]
lis(l)
