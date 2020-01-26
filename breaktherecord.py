n=int(input())
l=[int(i) for i in input().strip().split(' ')]
maxcount=mincount=0
max=min=l[0]
for i in l:
    if i>max:
        max=i
        maxcount +=1
    elif i<min:
        min=i
        mincount +=1

print(maxcount,mincount)