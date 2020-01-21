count=0
n=int(input())
l=[int(i) for i in input().strip().split(' ')]
l.sort(reverse=True)
m=int(input())
l1=[int(i) for i in input().strip().split(' ')]
v=0
for i in l1:
    l.append(i)
    l.sort(reverse=True)
    x = count = abc = 0
    for j in l:
        if j != x:
            count += 1
            x = j
        if j == i:
            # print(l)
            if abc == count:
                pass
            else:
                print(count)
                abc = count




