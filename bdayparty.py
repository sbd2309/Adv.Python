def bday(n):
    l=[]
    if n==1:
        l.append(1)
    elif n==2:
        l.append(6)
    else:
        l.append(1)
        l.append(6)
        #pointer=23
        value=0
        for i in range(2,n,1):
            value=2*(l[i-1]+2)-l[i-2]
            #print(value)
            l.append(value)
    print(l[-1])
    #print(l)

n=int(input())
for i in range(0,n,1):
    n1=int(input())
    bday(n1)
