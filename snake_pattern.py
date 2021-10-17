n, m = (int(i) for i in input().strip().split(' '))
matrix = []
for i in range(n):
    l = [int(i) for i in input().strip().split(' ')]
    matrix.append(l)

for i in range(0,n,1):
    if i % 2 != 0:
        for j in range(m-1,-1,-1):
            print(matrix[i][j],end=" ")
    else:
        for j in range(0,m,1):
            print(matrix[i][j],end=" ")

    print(" ")

