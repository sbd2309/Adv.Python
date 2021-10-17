def familygame(n,s1):
    l=[]
    s2=s1*100
    for i in range(1,n+1,1):
        l.append(i)
    p=0
    for i in range(0,len(s2),1):
           if s2[i]=='y':
               l.pop(p)
               #print(l)
           else:
               p=p+1
           if p==len(l):
               p=0
           if len(l)==1:
               break
    print(l[0])


n=int(input())
s1=input()
familygame(n,s1)