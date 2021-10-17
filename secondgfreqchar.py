def sndfc(s):
    d = {}
    for i in range(0, len(s), 1):
        count = 0
        for j in s:
            if s[i] == j:
                count += 1
        d[s[i]] = count
    print(d)
    l=[]
    for i in d.values():
        l.append(i)
    l.sort()
    x=l[len(l)-2]
    if x!=1:
     for key,value in d.items():
        if value==x:
            print(key)
            break
    else:
        print("No Second most frequent character")




s = input()
sndfc(s)
