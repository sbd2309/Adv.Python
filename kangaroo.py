l=[int(i) for i in input().strip().split(' ')]
n=0
s=l[0]
s1=l[2]
while n<=10000:
    s=s+l[1]
    s1=s1+l[3]
    if s==s1:
        print ("YES")
        break
    n =n+1
if n==10001:
    print("NO")