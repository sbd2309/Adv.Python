def check_ams(n):
    n1=n
    sum=0
    while(n1!=0):
        r=n1%10
        sum=sum+r**3
        n1=n1//10
    if sum==n:
        print("amstrong")
    else:
        print("Not Amstrong")


n=int(input())
check_ams(n)