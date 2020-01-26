string1=input()
string2=input()
list1=string1.strip().split(' ')
list2=string2.strip().split(' ')
for i in list1:
    for j in list2:
        x=int(i)
        y=int(j)
        t=(x,y)
        print("{} ".format(t) ,end="")