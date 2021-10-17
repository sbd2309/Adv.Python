def multiple_ten(l):
    l1=[]
    l2=[]
    s1=''
    for i in l:
        if i%10!=0:
            l1.append(i)
        else:
            l2.append(i)
    for i in l2:
        l1.append(i)
    print(l1)


n=input().strip()
l=[int(i) for i in input().strip().split(' ')]

multiple_ten(l)