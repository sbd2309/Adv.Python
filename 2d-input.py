r=int(input())
c=int(input())

matrix=[]
for i in range(0,r,1):
    a=[]
    for j in range(0,c,1):
        a.append(int(input()))
    matrix.append(a)

for i in range(0,r,1):
    for j in range(0,c,1):
        print(matrix[i][j],end=" ")
    print()

mat=[[int(input()) for i in range (c)] for j in range(r)]
print(mat)
