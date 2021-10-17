def prime_pair(n, n1):
    l = []
    for i in range(n, n1 + 1, 1):
        flag = 0;
        for j in range(2, int(i / 2), 1):
            if i % j == 0:
                flag = 1
                break
        if (flag == 0):
            l.append(i)
    print(l)
    count = 0
    x = 1
    for i in l:
        for j in range(x, len(l), 1):
            if l[j] - i == 6:
                count += 1
        x += 1

    print(count)


n = int(input())
n1 = int(input())

prime_pair(n, n1)
