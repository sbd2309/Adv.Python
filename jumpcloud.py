def cloud_jump(l):
    count=0
    length=0
    while length< len(l)-1:
        if l[length] == 1:
            count+=1
        elif l[length] == 0:
            if l[length+1] == 1:
                count+=1
        length+=1
    if l[-1]==l[-2]:
        count+=1
    print(count)




n=int(input())
l=[int(i) for i in input().strip().split(' ')]
cloud_jump(l)