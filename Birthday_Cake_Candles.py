n=int(input().strip())
l=[int(i) for i in input().strip().split(' ')]

l.sort()
count=0
max=l[-1]
for i in l:
    if i==max:
        count+=1
print (count)