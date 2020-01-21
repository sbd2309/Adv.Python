s=input()
nkey=s.strip().split(' ')[1]
lkey=[int(i)  for i in input().strip().split(' ')]
nusb=s.strip().split(' ')[2]
lusb=[int(i) for i in input().strip().split(' ')]
money=int(s.strip().split(' ')[0])
s=0
for i in lkey:
    for j in lusb:
        if s < (i+j) and (i+j) <=money :
            s=i+j

if s==0:
    print(-1)
else:
    print(s)
