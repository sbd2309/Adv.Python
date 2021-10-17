def count_hill(s1):
    count=0
    s=0
    flag=0
    for i in s1:
        if i == 'U':
            s=s+1
        else:
            s=s-1
        if s<0:
            flag=1
        elif s>=0 and flag==1:
            count+=1
            flag=0
    print(count)


n=int(input())
s=input()
count_hill(s)