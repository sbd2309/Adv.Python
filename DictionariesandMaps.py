n=int(input())
d={}
for i in range(0,n,1):
    s=input()
    name=s.strip().split(' ')[0]
    pnum=s.strip().split(' ')[1]
    d.update({name:pnum})
l=[]
takename='Author:SoumyaDutta'
for i in range(0,n,1):
    takename=input()
    if takename!='':
        l.append(takename)
for i in l:
    flag=0
    for key,value in d.items():
        if i==key:
            print("{}={}".format(key,value))
            flag=1
    if flag==0:
        print("Not Found")



