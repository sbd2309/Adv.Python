def factorialbaap(f,p):
    n=1
    for i in range (f,0,-1):
        n=n*i
    #print(n)
    x=p
    flag=0
    ans=0
    while 1==1:
        for i in range (1,1000,1):
            x=p**i
            if n%x==0:
                ans=i
            elif x>n:
                flag=1
                break
        break

    if flag==1 and ans!=0:
        print(ans)
    else:
        print(0)

n=int(input())
for i in range(0,n,1):
    x,y =[int(i) for i in input().strip().split(' ')]
    factorialbaap(x,y)







