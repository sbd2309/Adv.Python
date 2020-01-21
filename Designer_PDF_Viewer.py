n=input()
l=[int(i) for i in input().strip().split(' ')]
al=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
d={}
x=0
for i in l:
    d.update({al[x]:i})
    x+=1

print(d)