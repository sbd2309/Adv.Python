n=input()
l=[]
for i in n:
    l.append(int(i))


for i in range(0,len(n),1):
    temp=n[i]
    for j in range(i+1,len(n),1):
        temp=temp+n[j]
        l.append(int(temp))

print(sum(l))