l=[int(i) for i in input().strip().split(' ')]

l.sort()
x=0
l2=[]
for i in range(0,len(l),1):
    l2.append((sum(l) - l[x]))
    x+=1

l2.sort()
print(l2[0],l2[-1])