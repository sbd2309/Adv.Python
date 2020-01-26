s=input()
index1=int(s.strip().split(' ')[0])
index2=int(s.strip().split(' ')[1])
l=[]
for i in range(index1,index2+1,1):
    l.append(i)
k=int(s.strip().split(' ')[2])
l1=[]
for i in l:
    cs=str(i)
    l1.append(cs[::-1])
#print(l1)
x=0
count=0
while x<len(l):
    #print(abs(int(l[x]) - int(l1[x]))%k)
    if abs(int(l[x]) - int(l1[x]))%k==0:
        count+=1
    x+=1
print(count)