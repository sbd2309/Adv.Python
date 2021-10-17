def right_rotate(l, k):
    #l1 = []
    #x = l[0]
    #l1.append(x)
    for j in range(1, k+1, 1):
        l1 = []
        x = l[0]
        l1.append(x)
        l1.append(l[-1])
        for i in range(1, len(l) - 1, 1):
            l1.append(l[i])
        print(l1)
        l = l1
    print(l)


n = input().strip()
l = [int(i) for i in input().strip().split(' ')]
k = int(input())

right_rotate(l, k)
