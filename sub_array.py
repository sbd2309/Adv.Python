def sub_array(l):
    le = len(l)
    l1 = []
    for i in range(k, le , 1):
        l1.append(l[i])
    for i in range(0, k, 1):
        l1.append(l[i])
    print(l1)


n = input().strip()
l = [int(i) for i in input().strip().split(' ')]
k = int(input())

sub_array(l)
