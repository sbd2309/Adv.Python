def func(s):
    t=tuple(s)
    #print(t)
    l=[]
    for i in s:
        if i not in l:
            l.append(i)
    d={}
    l1=[]
    for i in l:
        count=t.count(i)
        d[i]=count
        l1.append(count)
    print(d)
    l1.sort()
    x=l1[len(l1)-2]
    if x!=1:
     for key,value in d.items():
        if value==x:
            print(key)
    else:
        print("No Second most frequent character")


s=input()
func(s)