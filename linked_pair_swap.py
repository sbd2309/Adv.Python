def pair_swap(l):
    if len(l)%2==0:
        for i in range(0,len(l),2):
            x=l[i]
            y=l[i+1]
            l[i]=y
            l[i+1]=x
        for i in l:
            print(i)
    else:
        for i in range (0,len(l)-1,2):
            x = l[i]
            y = l[i + 1]
            l[i] = y
            l[i + 1] = x
        for i in l:
            print(i)

l=[]
while True:
    n=int(input())
    if n<0:
        break
    else:
        l.append(n)
pair_swap(l)