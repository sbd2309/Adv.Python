def check_pall(n):
    n1=n
    s1=''
    while n1!=0:
        r=n1%10
        s1=s1+str(r)
        n1=n1//10
    if s1==str(n):
        print("Pallindrome")
    else:
        print("Not Pallindrome")


n=int(input())
check_pall(n)