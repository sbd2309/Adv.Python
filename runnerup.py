n=int(input().strip())
l=[int(i) for i in input().strip().split(' ')]

l.sort(reverse=True)
x=0
y=l[0]
for i in l:
    if y == i:
        pass
    else:
        if x < i:
            x=i

print(x)
