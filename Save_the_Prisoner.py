n=int(input())
l=[]
for i in range(0,n,1):
    s=input()
    prisoners=int(s.strip().split(' ')[0])
    toffee=int(s.strip().split(' ')[1])
    start=int(s.strip().split(' ')[2])
    dangerp=0
    while toffee>0:
        if start==prisoners:
            dangerp=prisoners
            start=1
            toffee-=1
            #print(dangerp)
        else:
            dangerp = start
            toffee -= 1
            start += 1

    l.append(dangerp)
for i in l:
    print(i)

