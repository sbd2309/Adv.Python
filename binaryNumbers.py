n=int(input())
counter=n
l=[]
onecount=0
while counter>=1:
    l.append(counter)
    counter=int(counter/2)
n1=[]
for i in l:
    if i % 2==0:
        n1.append(0)
    else:
        n1.append(1)
n1.reverse()
#print(n1)
count=0
for i in n1:
    if i==1:
        count+=1
    else:
        if onecount<count :
            onecount=count
        count=0
if count<onecount:
    print(onecount)
else:
    print(count)