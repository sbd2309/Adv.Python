inputstring=input()
c=''
l1=[]
for i in inputstring:
    if c!=i:
        c=i
        l1.append(c)
x=y=z=0
l=[]
for i in l1:
    number=int(i)
    count=0
    for j in range(x,len(inputstring),1):
        if number==int(inputstring[j]):
            z = int(inputstring[j])
            count+=1
            y+=1
        else:
            t = (count, z)
            l.append(t)
            x = y
            break
        if y==len(inputstring):
            t=(count,z)
            l.append(t)
for i in l:
    print(i,end=" ")

from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])