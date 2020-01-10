n=input().strip()
st=input()
s=0
count=0
flag=0
for i in st:
    if i == 'U':
        s=s+1
    else:
        s=s-1
    if s<0:
        flag=1
    elif flag==1 and s>=0:
        flag=0
        count+=1
#print(s)
print(count)