n=int(input().strip())

l=[int(i) for i in input().strip().split(' ')]
l1=[int(i) for i in input().strip().split(' ')]
#print (l,l1)
x=0
d={}
for i in l:
   d.update({l[x]:l1[x]})
   x+=1

#print (d)
s=0
for key,value in d.items():
   s=s+(key*value)

print (s/sum(l1))
