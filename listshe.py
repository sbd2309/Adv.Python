l=[]
n=int(input())
for i in range(0,n,1):
    s=input()
    l.append(s.strip().split(' '))
l1=[]
for i in l:
    if len(i)==3:
        l1.insert(int(i[1]),int(i[2]))
    elif i[0]=='print':
        print(l1)
    elif i[0]=='remove':
        l1.remove(int(i[1]))
    elif i[0]=='append':
        l1.append(int(i[1]))
    elif i[0]=='sort':
       # print(l1)
        l1.sort()
    elif i[0]=='pop':
        l1.pop()
    elif i[0]=='reverse':
        l1.reverse()



