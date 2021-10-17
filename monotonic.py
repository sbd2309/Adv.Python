l=[int(i) for i in input().strip().split(' ')]
l.append(-1)
flag =0
for i in range(0,len(l),1):
    if l[i+1] == -1:
        break
    if l[i] <= l[i+1]:
        continue
    else:
        print(l[i])
        flag =1
        break

if flag==1:
    flag=0
    for i in range(0, len(l), 1):
        if l[i + 1] == -1:
            break
        if l[i] >= l[i + 1]:
            continue
        else:
            flag = 1
            break

if flag == 0:
    print("true")
else:
    print("false")

