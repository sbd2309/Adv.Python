def fairRations(B):
    c = 0
    m = 0
    for i in range(len(B)):
        c+=B[i]
        print(c)
        if c % 2 == 1:
            m+=2
    if c % 2 != 0:
        return 'NO'
    else:
        return m


N = int(input())
B = list(map(int, input().rstrip().split()))
result = fairRations(B)
print(result)