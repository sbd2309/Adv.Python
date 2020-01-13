n=int(input().strip())
l=[int(i) for i in input().strip().split(' ')]
l.sort()
x=int(len(l)/2)
l1=[]
l2=[]
if n%2 !=0 :
    a=0
    for i in l:
        if a==x:
            pass
        elif a<=x:
            l1.append(i)
        else:
            l2.append(i)
        a+=1
    #print (l1,l2)
mid1=int(len(l1)/2)
mid2=int(len(l2)/2)
print ((l1[mid1] + l1[mid1-1])/2)
print(l[x])
print ((l2[mid2] + l2[mid2-1])/2)