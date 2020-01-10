n=int(input().strip())
n1=n
for i in range(1,n+1,1):
    for j in range(n1,-1,-1):
        print(" ",end="")
    n1=n1-1
    for k in range(1,i+1,1):
        print("*",end="")
    print("\n")
