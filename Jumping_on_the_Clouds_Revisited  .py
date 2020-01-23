n=input()
noc=n.strip().split(' ')[0]
l=[int(i) for i in input().strip().split(' ')]
jump=int(n.strip().split(' ')[1])
index=1
value=100
x=0
while index!=0:
    if x==0:
        index=0
        x+=1
    index=index+jump
    if index>=len(l):
        index=index-len(l)
    if l[index] == 1:
        value = value - 3
    elif l[index]==0:
        value = value - 1
print(value)    
