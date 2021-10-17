def naughty_students(l):
    d = {}
    t = tuple(l)
    for i in l:
        temp = t.count(i)
        d[i] = temp
    #print(d)
    s_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    temp_list = []
    #print(s_d)
    i = 0
    for j in range(0, len(s_d), 1):
        # print(i)
        if i + 1 < len(s_d):
            if s_d[i][1] == s_d[i + 1][1]:
                temp_list.append(s_d[i])
                temp_list.append(s_d[i + 1])
                temp_list.sort()
                for j in temp_list:
                    print("{} {}".format(j[0],j[1]))
                temp_list = []
                i = i + 2
            else:
                print("{} {}".format(s_d[i][0],s_d[i][1]))
                i = i + 1
        elif i < len(s_d):
            print("{} {}".format(s_d[i][0],s_d[i][1]))
            i = i + 1


n = int(input())
l = []
for i in range(0, n, 1):
    t_i = input()
    l.append(t_i)
naughty_students(l)
