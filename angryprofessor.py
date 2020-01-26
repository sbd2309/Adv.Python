n=int(input())
for i in range(0,n,1):
    firstline=input()
    sndline=input()
    attendance=int(firstline.strip().split(' ')[0])
    mattendance=int(firstline.strip().split(' ')[1])
    l=sndline.strip().split(' ')
    count=0
    for j in l:
        if int(j)<=0:
            count+=1
    if count >=mattendance:
        print("NO")
    else:
        print("YES")

