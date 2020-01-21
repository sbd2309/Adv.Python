n=int(input().strip())
l=[]
for i in range(0,n,1):
    l.append(input().strip())
st=st1=''
for i in l:
    s=i
    x=0
    for j in s:
        if x%2==0:
            st=st+j
            x+=1
        else:
            st1=st1+j
            x+=1
    print("{} {}".format(st,st1))
    st=st1=''



