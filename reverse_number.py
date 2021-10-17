def reverse_num(n):
    s1=''
    while n!=0:
        r=n%10
        s1=s1+str(r)
        n=n//10
    num=int(s1)
    print (num)


n=int(input())
reverse_num(n)


