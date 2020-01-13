import math

n=int(input().strip())
l=[int(i) for i in input().strip().split(' ')]
#print(len(l))
mean=(sum(1)/n)
#print(l[mid])
s=0
x=0
for i in l:
    s=s+((l[x]-mean)**2)
    #print (s)
    x+=1

x=s/n
print ("{:.1f}".format(math.sqrt(x)))