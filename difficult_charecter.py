def diff_char(st):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    alpha.reverse()
    t = tuple(st)
    d = {}
    l = []
    for i in alpha:
        if i in t:
            temp = t.count(i)
            x = temp, i
            l.append(x)
            d[i] = temp
    l.sort()
    # print(l)a
    l_temp = []
    flag = 0
    for i in alpha:
        if i not in t:
            print(i, end=" ")
    '''for i in l:
        print(i[1],end=" ")'''
    # print(l)
    '''for i in l:
        print(i[1],end=" ")'''
    # print(l)
    i = 0
    j = 0
    while i < len(l):
        # print(i)
        if j < len(l):
            if l[i][0] == l[j][0]:
                l_temp.append(l[j])
                j += 1
                flag = 1
            elif flag == 1:
                i = j
                l_temp.reverse()
                for k in l_temp:
                    print(k[1], end=" ")
                # print(l_temp)
                flag = 0
                l_temp = []
        else:
            print(l[i][1], end=" ")
            i += 1


n = int(input())
for i in range(0, n, 1):
    st = input()
    diff_char(st)
