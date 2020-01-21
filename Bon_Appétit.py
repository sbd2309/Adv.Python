s=input()
i=int(s.split(' ')[0])
l=[int(k) for k in input().strip().split(' ')]
paid=int(input())
j=int(s.split(' ')[1])
x=s=0
for i in l:
    if x==j:
        x+=1
        pass
    else:
        x+=1
        s=s+i
if s/2== paid:
    print("Bon Appetit")
else:
    print(int(paid-(s/2)))
