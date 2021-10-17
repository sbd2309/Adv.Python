def allzeroallone(l):
    t=tuple(l)
    x=t.count(0)
    y=t.count(1)
    l1=[]
    for i in range (0,x,1):
        l1.append(0)
    for i in range (0,y,1):
        l1.append(1)
    for i in l1:
        print(i,end=" ")





n=int(input())
l=[int(i) for i in input().strip().split(' ')]
allzeroallone(l)