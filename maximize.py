s=input()
l=s.strip().split(' ')[0]
k=s.strip().split(' ')[1]
l3=[]
l2=[]
l1=[]
for i in range(0,int(l[0]),1):
    s1=input()
    l1=s1.strip().split(' ')
    x=int(l1[0])
    for z in range(1,x+1,1):
        l2.append(int(l1[z]))
    l3.append(max(l2)*max(l2))
    l2=[]
print(l3)
print(sum(l3)%int(k))



