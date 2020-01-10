n=int(input().strip())

l=[int(i) for i in input().strip().split(' ') ]
x=0
#y=1
count=0
while n>=1:
    if n>1 and l[x]==l[x+1] and l[x+1]==l[x+2]:
        count+=1
        #print(count)
        x=x+2
        n=n-3
        #print(n)
    elif n>1 and l[x]==0 and l[x+1]==0:
        count+=1
        #print(count)
        x=x+1
        n=n-1
        #print(n)
    elif l[x]!=l[x+1]:
        x=x+2
        n=n-2
        count+=1

        #print(count)
        #print(n)

print (count)
