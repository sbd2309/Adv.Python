import random
class sort():
    def __init__(self):
        pass
    def sortme(self,l):
        l3=[]
        l2=[]
        print (l)
        while len(l)>=1:
            #print (len(l))
            x = 1001
            for i in l:
                # print (i)
                if x >= int(i):
                    x = int(i)
            l3.append(x)
            for i in l:
                if int(i) == x:
                    continue
                else:
                    l2.append(int(i))

            l = l2
            l2 = []
        print (l3)

i_sort=sort()
#l=[5,4,3,2,1]
l=[]
n=int(input("How many numbers you want to input: "))
i=0
while i<=n:
    l.append(random.randint(500,1000))
    i +=1
i_sort.sortme(l)


