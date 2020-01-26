n=int(input())
initial=5
l=[]
x=0
while x<n:
    c=int(initial/2)
    l.append(c)
    initial=c*3
    x+=1
print(sum(l))