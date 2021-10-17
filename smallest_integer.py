n = int(input())


class si():
    def __init__(self):
        pass

    def sinteger(self, n):
        l = []
        for i in range(1, int(n / 2) + 1, 1):
            if n % i == 0:
                l.append(i)
        print(l)
        temp=[]
        # l.append(-1)
        if n < 100:
            for i in range(0, len(l), 1):
                for j in range(i, len(l), 1):
                    if l[i] * l[j] == n:
                        st=str(l[i])+str(l[j])
                        temp.append(int(st))
            #temp.sort()
            #print(temp[0])
        elif n >= 100 and n < 1000:
            for i in range(0, len(l), 1):
                for j in range(i, len(l), 1):
                    if l[i] * l[i] * l[j] == n:
                        st=str(l[i])+str(l[i])+str(l[j])
                        temp.append(int(st))
            for i in range(0, len(l), 1):
                for j in range(i, len(l), 1):
                    if l[i] * l[j] * l[j] == n:
                        st = str(l[i]) + str(l[j])+ str(l[j])
                        temp.append(int(st))
        temp.sort()
        print(temp)
        if len(temp)>0:
            print(temp[0])
        else:
            print("Not Possible")


x = si()
x.sinteger(n)
