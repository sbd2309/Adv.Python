st=input().strip()
n=int(st.split(' ')[0])
l=[int(i) for i in input().strip().split(' ')]
k=int(st.split(' ')[1])
x=count=0
for i in l:
    x+=1
    for j in range(x,len(l),1):
        if (i+l[j])%k ==0:
            count+=1

print(count)


