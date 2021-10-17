n = int(input())
l1 = []
for i in range(0, n, 1):
    l = [str(i) for i in input().strip().split(' ')]
    l1.append(l)


class fl():
    def __init__(self):
        pass

    def table(self, l):
        d = {}
        for i in range(0, len(l), 1):
            d[l[i][0]] = 0
        #print(d)
        for i in range(0, len(l), 1):
            temp_score = l[i][2]
            temp_s1 = int(temp_score[0])
            temp_s2 = int(temp_score[2])
            if temp_s1 > temp_s2:
                d[l[i][0]] += 3
            elif temp_s1 < temp_s2:
                d[l[i][1]] += 3
            elif temp_s1 == temp_s2:
                d[l[i][0]] += 1
                d[l[i][1]] += 1
        max=0
        name=''
        for x,y in d.items():
            if max<y:
                max=y
                name=x
        print("Winner {} : {}".format(name,max))






x = fl()
x.table(l1)
