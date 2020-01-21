n=int(input())
l=[int(i) for i in input().strip().split(' ')]
l.sort()
count=0
d={}
uniq=[]
for i in l:
    if i not in uniq:
        uniq.append(i)
for i in uniq:
    for j in l:
        if i==j:
            count+=1
    d.update({i:count})
    count=0
d1={}
for i in sorted(d):
    d1.update({i:d[i]})
#print(d1)
max=0
for key,value in d1.items():
    if max<value:
        max=value
        hkey=key
print(hkey)
