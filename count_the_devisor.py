def ctd(l):
    l1=[]
    for i in l:
        s1=str(i)
        count=0
        for j in s1:
            if j =='0':
                pass
            elif i%int(j) ==0:
                count+=1
        print(f"{count}")
        l1.append(count)
    print(l1)

n=int(input())
l=[]
for i in range (0,n,1):
    x=int(input())
    l.append(x)
ctd(l)
