s=input()
take_hudles=s.strip().split(' ')[0]
l=[int(i) for i in input().strip().split(' ')]
height=int(s.strip().split(' ')[1])
count=0
for i in l:
    if i>height:
        count+=1
print(count)