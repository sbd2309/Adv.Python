def rotate_matrix(l, y):
    l1=[]
    for i in range(0, y, 1):
        l1.append(l[-1])
        for j in range(0, len(l) - 1, 1):
            l1.append(l[j])
        l = l1
        l1=[]
    for i in l:
        print(i)


x, y = [int(i) for i in input().split()]
l = [int(i) for i in input().strip().split(' ')]

rotate_matrix(l, y)
