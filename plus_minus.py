n=int(input().strip())
l=[int(i) for i in input().strip().split(' ')]
p=n1=z=0
for i in l:
    if i>0:
        p+=1
    elif i<0:
        n1+=1
    else:
        z+=1

print(round(float(p/n),6))
print(round(float(n1/n),6))
print(round(float(z/n),6))