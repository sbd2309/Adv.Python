n=input().strip()
l=[int(i) for i in input().strip().split(' ')]
l1=[int(i) for i in input().strip().split(' ')]
d={}
x=0
for i in l:
    d.update({l[x]:l1[x]})
    x+=1
#print(d)
d1={}
for i in sorted (d) :
    d1.update({i:d[i]})

#print(d1)
l2=[]
for key,value in d1.items():
    for i in range(0,value,1):
     l2.append(key)

#print(l2)
l3=[]
l4=[]
if len(l2)%2==0:
    for i in range(0,int(len(l2)/2),1):
        l3.append(l2[i])
    for i in range(int(len(l2)/2),len(l2),1):
        l4.append(l2[i])
    #print(l3,l4)
    mid1=int(len(l3)/2)
    mid2=int(len(l4)/2)
    x=(l3[mid1] + l3[mid1-1])/2
    y=(l4[mid2] + l4[mid2-1])/2
    print(y-x)
else:
    for i in range(0,int(len(l2)/2),1):
        l3.append(l2[i])
    for i in range(int(len(l2)/2),len(l2),1):
        l4.append(l2[i])
    #print(l3,l4)
    mid1=int(len(l3)/2)
    mid2=int(len(l4)/2)
    x=(l3[mid1] + l3[mid1-1])/2
    y=(l4[mid2] + l4[mid2-1])/2
    print(y-x)




