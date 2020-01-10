st=input()
l=[]
ns=''
r=''
count=0
for i in st:
    if i=='A' or i=='P':
        r=i
        l.append(ns)
        break
    elif i!=':':
        ns=ns+i
        #print(ns)
    else:
        l.append(ns)
        ns =''
print(l)
t=int(l[0])
if r=='A':
    x=0
    for i in l:
        if x == len(l) - 1:
            print('{}'.format(i), end="")
            x+=1
        else:
            print('{}:'.format(i), end="")
            x += 1
else:
    x=0
    for i in l:
       if x==0:
           print('{}:'.format(t+12),end="")
           x+=1
       else:
           if x == len(l)-1:
               print('{}'.format(i), end="")
           else:
            print('{}:'.format(i),end="")
            x+=1
