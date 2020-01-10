#n=int(input().strip())

l=[int(i) for i in input().strip().split(' ')]
l1=[int(i) for i in input().strip().split(' ')]
x=0
a=b=0
for i in l1:
    if l[x]==l1[x]:
        x+=1
        pass
    elif l[x]>l1[x]:
        a+=1
        x+=1
    else:
        b+=1
        x+=1

print(a,b)

