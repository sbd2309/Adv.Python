n, m = (int(i) for i in input().strip().split(' '))


def kaprekar(n, m):
    for i in range(n, m + 1, 1):
        cp = pow(i, 2)
        st = str(cp)
        s1 = st[0:len(st) // 2]
        s2 = st[len(st) // 2:len(st)]
        x = int(s1) + int(s2)
        if x == i:
            print(i)


kaprekar(n, m)

'''n=int(input())
cp=pow(n,2)
st=str(cp)
s1=st[0:len(st)//2]
s2=st[len(st)//2:len(st)]
x=int(s1)+int(s2)
print(x)'''
