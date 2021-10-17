n = input()
l = [int(i) for i in input().strip().split(' ')]
l.append(-1)


def seq(l):
    sum = 0
    max = 0
    for i in range(0, len(l), 1):
        if l[i] == -1:
            break
        if l[i] < l[i + 1]:
            sum = sum + l[i]
        else:
            sum = sum + l[i]
            if max < sum:
                max = sum
            sum = 0
    print(max)


seq(l)
