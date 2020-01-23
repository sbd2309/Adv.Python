n=int(input())
for i in range(0,n,1):
    l=[]
    count=0
    number=input()
    for j in number:
        l.append(int(j))
    for k in l:
        if k==0:
            pass
        elif int(number)%k==0:
            count+=1
    print(count)
    