bpages=int(input())
tpage=int(input())
flag=tpage
flag1=0
count=count1=0
while tpage+1 < bpages:
    tpage+=2
    count+=1

while flag1 < flag:
    flag1+=2
    count1+=1

if count1<count:
    print(count1)
else:
    print(count)