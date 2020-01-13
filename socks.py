n = int(input().strip())

l = [int(i) for i in input().strip().split(' ')]
ul=[]
for i in l:
    if i not in ul:
        ul.append(i)
count=0
sock=0
for i in ul:
    count=0
    for j in l:
        if j==i:
            count +=1
            if count==2:
                sock=sock+1
                count=0
print(sock)