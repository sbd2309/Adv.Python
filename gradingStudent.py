n=int(input().strip())
l=[]
for i in range(0,n,1):
    x=int(input())
    l.append(x)

print(l)

for i in l:
    if i>=38:
        if 5-i%5 >= 3:
            print(i)
        else:
            print(i+(5-i%5))
    else:
        print(i)

