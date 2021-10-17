def findnum(s):
    s=s+' '
    l=[]
    s1=''
    for i in s:
        if i==' ':
            l.append(s1)
            s1=''
        else:
            s1=s1+i
    num_list=['1','2','3','4','5','6','7','8','0']
    num_list_2=[]
    for i in l:
        flag=0
        for j in i:
            if j in num_list and j!='9':
                flag=0
            else:
                flag=1
                break
        if flag == 0:
            num_list_2.append(i)

    l1=[]
    for i in num_list_2:
        l1.append(int(i))
    y=max(l1)
    print(y)

n=int(input())
s=input()
findnum(s)
