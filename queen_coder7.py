l=[int(i) for i in input().strip().split(' ')]
n=int(input())

l.sort(reverse=True)
#print(l)
print(l[-n])
