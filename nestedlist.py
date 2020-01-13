n=int(input().strip())
l=[]
l1=[]
for i in range(0,n,1):
    l.append(input())
    l1.append(float(input()))
x=0
d={}
for i in l:
    d.update({l[x]:l1[x]})
    x+=1
d1={}
for i in sorted(d):
    d1.update({i:d[i]})

x=min(d1.values())
y=max(d1.values())
for key,value in d1.items():
    if value==x:
        pass
    elif y > value:
        y=value
#print(y)
l2=[]
for key,value in d1.items():
    if y==value:
        l2.append(key)
for i in l2:
    print(i)





