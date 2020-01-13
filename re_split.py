s=input()
ns=''
for i in s:
    if i!=',' and i!='.':
        ns=ns+i
        #print(ns)
    else:
        print(ns)
        ns=''
print(ns)