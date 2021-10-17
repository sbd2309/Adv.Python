l=[str(i) for i in input().strip().split(' ')]
d={}
t=tuple(l)
for i in l:
    temp=t.count(i)
    d[i]=temp

print(d)