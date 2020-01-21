n=input()
l=n.strip().split(' ')
pdf=input()
al=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
d={}
x=0
for i in l:
    d.update({al[x]:int(i)})
    x+=1
height=0
for i in pdf:
    for key,value in d.items():
        if i==key:
            if height<value:
                height=value

print(len(pdf)*height)
