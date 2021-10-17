def delete(l,x):
    l1=[]
    for i in l:
        l1.insert(0,i)
    if x < len(l):
        print(l1[-x])
    else:
        print("No node found")

n=int(input())
l=[int(i) for i in input().strip().split(' ')]
index=int(input())
delete(l,index)