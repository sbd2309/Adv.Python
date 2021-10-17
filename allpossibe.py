
def allpossibe(s):
    for i in range(0,len(s),1):
        if s[i] in s[i+1:]:
            print("Contains duplicate elements!")
            break
    l=[]
    for i in range(0,len(s),1):
        s1=s[i]
        for j in range (0,len(s),1):
            if i==j:
                pass
            else:
                s1=s1+s[j]
        l.append(s1)
        s1=s[i]
        for j in range (len(s)-1,-1,-1):
            if i==j:
                pass
            else:
                s1=s1+s[j]
        l.append(s1)

    print(l)




s=input()
allpossibe(s)