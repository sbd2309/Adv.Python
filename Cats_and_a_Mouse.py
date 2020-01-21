n=int(input())
fl=[]
for i in range(0,n,1):
    s=input()
    count=count1=0
    l=s.strip().split(' ')
    a=int(l[0])
    b=int(l[1])
    c=int(l[2])
    if a<c:
        while a<c:
            a+=1
            count+=1
    else:
        while a>c:
            a-=1
            count+=1
    if b<c:
        while b<c:
            b+=1
            count1+=1
    else:
        while b>c:
            b-=1
            count1+=1
    if count==count1:
        fl.append("Mouse C")
    elif count<count1:
        fl.append("Cat A ")
    else:
        fl.append("Cat B")
for i in fl:
    print(i)

