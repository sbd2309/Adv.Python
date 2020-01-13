n=int(input().strip())
l=[str(i) for i in input().strip().split(' ')]
l1=[str(i) for i in input().strip().split(' ')]
l2=[str(i)for i in input().strip().split(' ')]
name=input().strip()


def cal_avg(l):
    x=0
    s=0.00
    for i in l:
        if x==0:
            x+=1
            pass
        else:
            s=s+float(i)
            x+=1
    print("{0:.2f}".format(s/3))

if name in l:
    cal_avg(l)
elif name in l1:
    cal_avg(l1)
else:
    cal_avg(l2)

