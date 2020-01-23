l1=[]
n=input()
arrlen=input()
l=arrlen.strip().split(' ')
nrotation=int(n.strip().split(' ')[1])
query=int(n.strip().split(' ')[2])
ql=[]
for i in range(0,query,1):
    q=int(input())
    ql.append(q)
x=0
while x<nrotation:
    l1 = []
    l1.append(l[-1])
    l.pop()
    for i in l:
        l1.append(i)
    x+=1
    l=l1
for i in ql:
    print(l1[i])