st=input()
st=st.lower()
rd=''
count=0
l=['a','e','i','o','u']
for i in range(0,len(st),1):
    if st[i] not in rd:
        rd=rd+st[i]
for i in range(0,len(l),1):
    if l[i] in rd:
        count+=1
if count == 5:
    print("Yes")
else:
    print("No")


